from typing_extensions import Literal
from dataclasses import dataclass
from decimal import Decimal

from trading_sdk.market.trading.place_order import (
  PerpPlaceOrder, Order as OrderTDK, OrderState
)

from dydx.node.private.place_order import Order, LimitOrder, MarketOrder
from dydx.sdk.core import TradingMixin, wrap_exceptions, perp_name
from dydx.sdk.market.user_data.query_order import query_order

@dataclass
class PlaceOrder(PerpPlaceOrder, TradingMixin):

  def parse_order(self, order: OrderTDK) -> Order:
    if order['type'] == 'LIMIT':
      return LimitOrder(
        type='LIMIT',
        side=order['side'],
        price=Decimal(order['price']),
        size=Decimal(order['qty']),
        flags=self.limit_flags,
        time_in_force='POST_ONLY' if order.get('post_only') else 'GOOD_TIL_TIME'
      )
    elif order['type'] == 'MARKET':
      return MarketOrder(
        type='MARKET',
        side=order['side'],
        size=Decimal(order['qty']),
        flags=self.market_flags,
      )
      
  @wrap_exceptions
  async def _place_order(
    self, instrument: str, /, *, order: Order,
    response: Literal['id', 'state'] = 'id'
  ) -> str | OrderState:
    market = await self.market(instrument)
    r = await self.node.place_order(market, self.parse_order(order), unsafe=True)
    id = r['order'].order_id.SerializeToString()
    if response == 'id':
      return id
    else:
      return await query_order(self.indexer_data, address=self.address, instrument=instrument, id=id)

  async def _perp_place_order(self, base: str, quote: str, /, *, order: Order, response: Literal['id', 'state'] = 'id') -> str | OrderState:
    instrument = perp_name(base, quote)
    return await self._place_order(instrument, order=order, response=response)
