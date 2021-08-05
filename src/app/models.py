import datetime
import logging

from sqlalchemy import Boolean, Column, String, ForeignKey, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID

# from app.database import Base
import uuid

from sqlalchemy.orm import relationship

from app.database import Base

logger = logging.getLogger(__name__)


class Todo(Base):
    """
    Table for todos.
    """
    __tablename__ = "todo"

    id = Column(
        Integer,
        primary_key=True,
        unique=True)
    title = Column(String(128), nullable=False)
    notes = Column(String(256), nullable=False)
    completed = Column(Boolean, nullable=False, default=False)
    owner_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    owner = relationship("User", back_populates="items")