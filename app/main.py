from fastapi import Depends, HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi import logger
import logging
import os

from app import crud, models, schemas
from app.database import SessionLocal, engine
from app.routers import todo


# Create tables on startup
models.Base.metadata.create_all(bind=engine)


# Setup logging
logger = logging.getLogger("gunicorn.error")

if not os.getenv("LOG_LEVEL"):

    logger.setLevel(logging.DEBUG)
else:
    try:
        # if it is invalid, set it to DEBUG
        logger.setLevel(os.getenv("LOG_LEVEL"))
    except:
        logger.setLevel(logging.DEBUG)
        logger.error(str(
            "Incorrect log level set - setting log level to DEBUG: {}".format(
                os.getenv("LOG_LEVEL")
            )))
        



app = FastAPI(
    title="Todo Rest API"
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","DELETE"],
    allow_headers=["*"],
)

app.include_router(todo.router)