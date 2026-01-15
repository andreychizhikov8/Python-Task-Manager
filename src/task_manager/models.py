from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass

class Task:
    id: int
    title: str
    created_at: datetime
    completed_at: Optional[datetime] = None
    progress: int = 0
    done: bool = False

    def __post_init__(self):
        if not self.title or len(self.title.strip()) == 0:
            raise ValueError("Task should have a title!")
        
        if self.progress > 100 or self.progress < 0:
            raise ValueError("Wrong value for progress!")
        
        if self.done and self.completed_at is None:
            self.completed_at = self.created_at

        if not self.done:
            self.completed_at = None
