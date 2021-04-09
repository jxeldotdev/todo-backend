from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import false, null
from sqlalchemy.sql.schema import UniqueConstraint

from app.database import Base

import uuid
import secrets

class Todo(Base):
    """
    Table for todos.
    """
    __tablename__ = "todo"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    title = Column(String(128), nullable=False)
    notes = Column(String(256), nullable=False)
    completed = Column(Boolean, default=False)