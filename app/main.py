from fastapi import Depends, HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from os import getenv
from fastapi import logger
import logging

from app import crud, models, schemas
from app.database import SessionLocal, engine
from app.routers import todo


# Create tables on startup
models.Base.metadata.create_all(bind=engine)


# Setup logging
gunicorn_logger = logging.getLogger('gunicorn.error')

logger.handlers = gunicorn_logger.handlers
if __name__ != "main":
    logger.setLevel(gunicorn_logger.level)
else:
    logger.setLevel(logging.DEBUG)


logger.setLevel()


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