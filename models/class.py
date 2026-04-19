from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class Class:
    id: Optional[int] = None
    class_name: str
    class_level: str
    school_year: str
    maximum_students: int = 50
    creation_date: str = field(default_factory=lambda: date.today().isoformat())