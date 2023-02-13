from datetime import datetime
from typing import Optional

from pydantic import BaseModel

# NOTE: These are Pydantic schemas that are used for request validation.
# These are not related  to the database.


class TodoDelete(BaseModel):
    pass


class TodoCreate(BaseModel):
    """
    Title: String
    Notes: (Optional): String
    Completed: Boolean

    """
    title: str
    notes: Optional[str] = None
    completed: bool = False

    class Config:
        orm_mode: True


class Todo(BaseModel):
    """
    id: integer
    Title: String
    Notes: (Optional): String
    Completed: Boolean
    created_at: datetime
    """
    
    id: int
    title: str
    notes: Optional[str] = None
    completed: bool = False
    created_at: datetime

    class Config:
        orm_mode: True

class TodoPut(TodoCreate):
    id: int
