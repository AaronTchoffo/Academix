from dataclasses import dataclass
from typing import Optional

@dataclass
class Subject:
    id: Optional[int] = None
    subject_name: str
    subject_weight: float = 1.0
    class_id: int
