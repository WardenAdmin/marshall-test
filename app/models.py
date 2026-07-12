from dataclasses import dataclass
from enum import Enum
from typing import List

class OrderStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class OrderItem:
    item_id: str
    quantity: int

@dataclass
class Order:
    order_id: str
    items: List[OrderItem]
    status: OrderStatus = OrderStatus.PENDING
    error_message: str | None = None
