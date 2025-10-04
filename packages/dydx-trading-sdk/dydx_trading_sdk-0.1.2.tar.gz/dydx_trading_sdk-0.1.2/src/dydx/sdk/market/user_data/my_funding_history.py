from typing_extensions import AsyncIterable, Sequence
from datetime import datetime
from dataclasses import dataclass

from trading_sdk.market.user_data.my_funding_history import (
  PerpMyFundingHistory, Funding
)

from dydx.core import timestamp as ts
from dydx.sdk.core import UserDataMixin, wrap_exceptions, perp_name

@dataclass
class MyFundingHistory(PerpMyFundingHistory, UserDataMixin):

  @wrap_exceptions
  async def my_funding_history(
    self, instrument: str, /, *,
    start: datetime, end: datetime
  ) -> AsyncIterable[Sequence[Funding]]:

    start = start.astimezone()
    end = end.astimezone()
      
    def within(t: datetime) -> bool:
      after = start is None or t >= start
      before = end is None or t <= end
      return after and before
    
    async for batch in self.indexer_data.get_funding_payments_paged(
      self.address, subaccount=self.subaccount, ticker=instrument, start=start
    ):
      fundings = [
        Funding(
          funding=f['payment'],
          time=t,
          side=f['side'],
          currency='USDC',
          rate=f['rate']
        )
        for f in batch
          if within(t := ts.parse(f['createdAt']))
      ]
      if fundings:
        yield fundings

  async def perp_my_funding_history(self, base: str, quote: str, /, *, start: datetime, end: datetime) -> AsyncIterable[Sequence[Funding]]:
    instrument = perp_name(base, quote)
    async for fundings in self.my_funding_history(instrument, start=start, end=end):
      yield fundings