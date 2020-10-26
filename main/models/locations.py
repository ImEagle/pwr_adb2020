from dataclasses import dataclass
from datetime import datetime


@dataclass
class Location:
    location_id: int
    name: str
    location_type: str
    country: str
    address: str
    latitude: float
    longitude: float
    created_at: datetime
