import logging

from sqlalchemy import Boolean, Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base
import uuid

from sqlalchemy.orm import relationship

logger = logging.getLogger(__name__)

class Todo(Base):
    """
    Table for todos.
    """
    __tablename__ = "todo"

    id = Column(
        UUID(
            as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True)
    title = Column(String(128), nullable=False)
    notes = Column(String(256), nullable=False)
    completed = Column(Boolean, nullable=False, default=False)
    # user_id = Column(UUID, ForeignKey("user.id"))

# class User(Base):
#     """
#     Table for users
#     """
#     __tablename__ = "user"
#
#     id = Column(
#         UUID(as_uuid=True),
#         primary_key=True,
#         default=uuid.uuid4,
#         unique=True,
#         index=True
#     )
#     name = Column(String(64), nullable=False, unique=True)
#     password_hash = Column(String(128))
#     todo_items = relationship("Todo")

