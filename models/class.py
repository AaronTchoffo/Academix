from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class Class:
    class_name: str
    class_level: str
    school_year: str
    id: Optional[int] = None
    maximum_students: int = 50
    creation_date: str = field(default_factory=lambda: date.today().isoformat())