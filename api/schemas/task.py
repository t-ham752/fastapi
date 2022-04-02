from typing import Optional
from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int = Field(example=1)
    title: Optional[str] = Field(None, example="Execute example todo")
    done: bool = Field(False, description="Done flag")
