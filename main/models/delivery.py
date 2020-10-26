from dataclasses import dataclass
from datetime import datetime


@dataclass
class Delivery:
    delivery_id: int
    order_id: int
    employee_id: int
    pick_up_at: datetime
    delivered_at: datetime
    type: str
    tip: float
