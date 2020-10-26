from dataclasses import dataclass
from datetime import datetime


@dataclass
class VendorCategory:
    vendor_category_id: int
    name: str
    is_seasonal: bool
    adults_only: bool
    created_at: str


@dataclass
class Vendor:
    vendor_id: int
    vendor_category_id: int
    location_id: int
    name: str
    delivery_charge: float
    is_open: bool
    created_at: datetime
