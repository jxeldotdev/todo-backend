from fastapi import Depends, HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
#from fastapi import logger
import logging
import os

from app import crud, models, schemas
from app.database import SessionLocal, engine
from app.routers import todo
from app.routers import health


# Create tables on startup
models.Base.metadata.create_all(bind=engine)

# # Setup logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)
# uvicorn_logger = logging.getLogger('uvicorn.error')
# logger.setLevel(uvicorn_logger.level)


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
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(todo.router, prefix="/todo")
app.include_router(health.router, prefix="/health")
