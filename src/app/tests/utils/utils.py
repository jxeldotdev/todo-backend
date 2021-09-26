import uuid

from app import models
from app.database import engine


def recreate() -> None:
    """
    Deletes and recreates the database tables.
    """
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)


def is_uuid(id: str) -> bool:
    """
    Checks if the string is a valid UUID
    """
    try:
        uuid.UUID(str(id))
        return True
    except ValueError:
        return False
