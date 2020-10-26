from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class CustomerLocation:
    customer_id: int
    location_id: int
    created_at: datetime

@dataclass
class Customer:
    customer_id: int
    gender: str
    date_of_birth: date
    is_active: bool
    created_at: datetime
    updated_at: datetime
    first_name: str
    last_name: str
