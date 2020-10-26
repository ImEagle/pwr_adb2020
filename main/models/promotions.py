from dataclasses import dataclass
from datetime import date


@dataclass
class PromotionItem:
    promotion_id: int
    item_id: int
    type: str
    min_items_count: int
    max_items_count: int
    discount_amount: float
    discount_percent: float


@dataclass
class Promotion:
    promotion_id: int
    vendor_id: int
    name: str
    start_date: date
    end_date: date
    type: str
    discount_amount: float
    discount_percent: float
