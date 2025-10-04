from dataclasses import dataclass
from .place_order import PlaceOrder
from .cancel_order import CancelOrder

@dataclass
class PrivateNode(PlaceOrder, CancelOrder):
  ...