from dataclasses import dataclass
from datetime import date


@dataclass
class Employee:
    employee_id: int
    first_name: str
    last_name: str
    access_code: str
    gender: str
    employment_date: date
    type: str
