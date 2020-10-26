from dataclasses import dataclass
from datetime import datetime


@dataclass
class Rating:
    rating_id: int
    order_id: int
    opinion: str
    rating: int
    created_at: datetime
