import logging
from typing import Any

from app import models
from app.database import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("", status_code=200)
def app_health(db: Session = Depends(get_db)) -> Any:
    """
    Checks database connection and returns 200 if it is OK
    """

    # Check database connection
    logger.debug("Running health check - selecting single todo from db")
    try:
        db.query(models.Todo).one()
    except NoResultFound as e:
        logger.info("No todos exist yet", e)
        success = True
    except SQLAlchemyError as e:
        logger.critical("Failed to return Todos in Health Check", exc_info=e)
        success = False

    if success:
        return HTTPException(200)
    else:
        return HTTPException(500)
