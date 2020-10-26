from dataclasses import dataclass
from datetime import datetime


@dataclass
class Item:
    item_id: int
    vendor_id: int
    name: str
    price: float
    created_at: datetime
