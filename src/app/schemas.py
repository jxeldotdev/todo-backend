from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

# NOTE: These are Pydantic schemas that are used for request validation.
# These are not related  to the database.


class TodoDelete(BaseModel):
    pass


class TodoCreate(BaseModel):
    title: str
    notes: Optional[str] = None
    completed: bool = False

    class Config:
        orm_mode: True


class Todo(BaseModel):
    id: int
    title: str
    notes: Optional[str] = None
    completed: bool = False

    class Config:
        orm_mode: True
