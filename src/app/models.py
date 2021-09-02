import datetime
import logging

from sqlalchemy import Boolean, Column, String, DateTime, Integer
from app.database import Base

logger = logging.getLogger(__name__)


class Todo(Base):
    """
    Table for todos.
    """

    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String(128), nullable=False)
    notes = Column(String(256), nullable=False)
    completed = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())
