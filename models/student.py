from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class Student:
    id: Optional[int] = None
    student_id: str
    last_name: str
    first_name: str
    birth_date: str
    parent_phone: Optional[str] = None
    class_id: int
    registration_date: str = field(default_factory=lambda: date.today().isoformat())
    is_active: bool = True

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"