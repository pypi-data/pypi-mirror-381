from dataclasses import dataclass

from trading_sdk.types import Num, fmt_num, ApiError
from trading_sdk.market.trading.edit_order import (
  SpotEditOrder, PerpEditOrder, InversePerpEditOrder
)

from dydx.sdk.core import (
  TradingMixin, wrap_exceptions, perp_name
)

@dataclass
class EditOrder(PerpEditOrder, TradingMixin):
  @wrap_exceptions
  async def edit_order(self, instrument: str, /, *, id: str, qty: Num | None = None, price: Num | None = None) -> str:
    def fmt(x: Num | None) -> str | None:
      if x is not None:
        return fmt_num(x)
    r = await self.client.edit(id, amount=fmt(qty), price=fmt(price))
    if not 'result' in r:
      raise ApiError(r['error'])
    else:
      return r['result']['order']['order_id']

  async def perp_edit_order(self, base: str, quote: str, /, *, id: str, qty: Num | None = None, price: Num | None = None) -> str:
    instrument = perp_name(base, quote)
    return await self.edit_order(instrument, id=id, qty=qty, price=price)