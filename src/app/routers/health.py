from typing import Any
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from app.database import get_db

from app import models, main

router = APIRouter()


@router.get("/", status_code=200)
def app_health(db: Session = Depends(get_db)) -> Any:
    """
    Checks database connection and returns 200 if it is OK
    """

    # Check database connection
    main.logger.info("Running health check - selecting single todo from db")
    try:
        db.query(models.Todo).one()
    except NoResultFound as e:
        main.logger.info("No todos exist yet", e)
        success = True
    else:
        success = True

    if success:
        return HTTPException(200)
    else:
        return HTTPException(500)
