from typing_extensions import AsyncIterable
from dataclasses import dataclass, field
from decimal import Decimal
from collections import defaultdict
import asyncio

from trading_sdk.market.user_streams.my_trades import (
  PerpMyTrades, Trade
)

from dydx.core import timestamp as ts
from dydx.sdk.core import UserStreamsMixin, wrap_exceptions, perp_name

@dataclass
class MyTrades(UserStreamsMixin, PerpMyTrades):
  _queues: defaultdict[str, asyncio.Queue[Trade]] = field(default_factory=lambda: defaultdict(asyncio.Queue), init=False, repr=False)
  _listener: asyncio.Task | None = field(default=None, init=False, repr=False)

  async def __aexit__(self, exc_type, exc_value, traceback):
    if self._listener is not None:
      self._listener.cancel()
      self._listener = None
    await super().__aexit__(exc_type, exc_value, traceback)

  @wrap_exceptions
  async def my_trades(self, instrument: str, /) -> AsyncIterable[Trade]:
    if self._listener is None:
      async def listener():
        _, stream = await self.indexer_streams.subaccounts(self.address, subaccount=self.subaccount)
        async for log in stream:
          if (fills := log.get('fills')):
            for fill in fills:
              if fill['ticker'] == instrument:
                trade = Trade(
                  id=fill['id'],
                  price=Decimal(fill['price']),
                  qty=Decimal(fill['size']),
                  time=ts.parse(fill['createdAt']),
                  side=fill['side'],
                  maker=fill['liquidity'] == 'MAKER',
                )
                self._queues[instrument].put_nowait(trade)
      self._listener = asyncio.create_task(listener())

    while True:
      # propagate exceptions raised in the listener
      t = asyncio.create_task(self._queues[instrument].get())
      await asyncio.wait([t, self._listener], return_when='FIRST_COMPLETED')
      if self._listener.done() and (exc := self._listener.exception()) is not None:
        raise exc
      yield await t

  async def perp_my_trades(self, base: str, quote: str, /) -> AsyncIterable[Trade]:
    instrument = perp_name(base, quote)
    async for trade in self.my_trades(instrument):
      yield trade
