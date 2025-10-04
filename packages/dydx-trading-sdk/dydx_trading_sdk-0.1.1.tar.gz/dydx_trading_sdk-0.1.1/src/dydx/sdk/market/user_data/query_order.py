from dataclasses import dataclass
from decimal import Decimal

from v4_proto.dydxprotocol.clob.order_pb2 import OrderId

from trading_sdk import ApiError
from trading_sdk.market.types.order import OrderState, OrderStatus as OrderStatusTDK
from trading_sdk.market.user_data.query_order import PerpQueryOrder

from dydx.core import timestamp as ts
from dydx.core.types import OrderStatus
from dydx.indexer.data import IndexerData
from dydx.sdk.core import UserDataMixin, wrap_exceptions, perp_name

def parse_status(status: OrderStatus) -> OrderStatusTDK:
  match status:
    case 'OPEN' | 'PENDING':
      return 'NEW'
    case 'CANCELED':
      return 'CANCELED'
    case 'FILLED':
      return 'FILLED'
    case 'UNTRIGGERED':
      return 'UNTRIGGERED'
    case _:
      raise ValueError(f'Unknown order status: {status}')

async def query_order(indexer_data: IndexerData, *, address: str, instrument: str, id: str) -> OrderState:
  order_id = OrderId.FromString(id)
  client_id = str(order_id.client_id)
  orders = await indexer_data.list_orders(address, ticker=instrument, unsafe=True)
  for o in orders:
    if o['clientId'] == client_id:
      return OrderState(
        id=id,
        price=Decimal(o['price']),
        qty=Decimal(o['size']),
        filled_qty=Decimal(o['totalFilled']),
        side=o['side'],
        time=ts.parse(o['updatedAt']),
        status=parse_status(o['status'])
      )
  
  raise ApiError(f'Order not found: {id}')

@dataclass
class QueryOrder(PerpQueryOrder, UserDataMixin):

  @wrap_exceptions
  async def query_order(self, instrument: str, /, *, id: str) -> OrderState:
    return await query_order(self.indexer_data, address=self.address, instrument=instrument, id=id)