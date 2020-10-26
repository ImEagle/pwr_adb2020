from dataclasses import dataclass
from datetime import datetime


@dataclass
class OrderItem:
    order_id: int
    item_id: int
    quantity: int
    comment: str


@dataclass
class Order:
    order_id: int
    customer_id: int
    employee_id: int
    vendor_id: int
    created_at: datetime
    status: str
    items_count: int
    total_amount: float
    promotion_id: int
    prepared_at: datetime
