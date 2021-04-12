from typing import List, Optional
import uuid

from pydantic import BaseModel, Field

# NOTE: These are Pydantic schemas that are used for request validation.
# These are not related  to the database.
class TodoDelete(BaseModel):
    pass

class TodoCreate(BaseModel):
    title: str 
    notes: Optional[str] = None
    completed: bool = None

    class Config:
        orm_mode: True

class Todo(BaseModel):
    id: str
    title: str 
    notes: Optional[str] = None
    completed: bool = None

    class Config:
        orm_mode: True