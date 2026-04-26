from dataclasses import dataclass
from typing import Optional

@dataclass
class Subject:
    class_id: int
    subject_name: str
    
    id: Optional[int] = None
    subject_weight: float = 1.0
