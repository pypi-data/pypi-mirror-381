from dataclasses import dataclass

from v4_proto.dydxprotocol.clob.order_pb2 import OrderId

from trading_sdk.types import ApiError
from trading_sdk.market.trading.cancel_order import PerpCancelOrder
from trading_sdk.market.user_data.query_order import OrderState

from dydx.sdk.core import TradingMixin, wrap_exceptions, perp_name
from dydx.sdk.market.user_data.query_order import query_order

@dataclass
class CancelOrder(PerpCancelOrder, TradingMixin):
  @wrap_exceptions
  async def cancel_order(self, instrument: str, /, *, id: str) -> OrderState:
    order_id = OrderId.FromString(id) # type: ignore
    await self.node.cancel_order(order_id, unsafe=True)
    return await query_order(self.indexer_data, address=self.node.address, instrument=instrument, id=id)

  async def perp_cancel_order(self, base: str, quote: str, /, *, id: str) -> OrderState:
    instrument = perp_name(base, quote)
    return await self.cancel_order(instrument, id=id)