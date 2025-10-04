from typing_extensions import Sequence
from dataclasses import dataclass

from trading_sdk.market.user_data.positions import (
  PerpPositions, Position
)

from dydx.sdk.core import UserDataMixin, wrap_exceptions, perp_name

@dataclass
class Positions(PerpPositions, UserDataMixin):

  @wrap_exceptions
  async def positions(self, instrument: str, /) -> Sequence[Position]:
    r = await self.indexer_data.list_positions(self.address, subaccount=self.subaccount, status='OPEN', unsafe=True)
    return [
      Position(
        side=p['side'],
        size=p['size'],
        entry_price=p['entryPrice'],
      )
      for p in r['positions']
        if p['market'] == instrument
    ]

  async def perp_positions(self, base: str, quote: str, /) -> Sequence[Position]:
    instrument = perp_name(base, quote)
    return await self.positions(instrument)