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
from app.config import TodoAppConfig

from app import cfg

# Create tables on startup
models.Base.metadata.create_all(bind=engine)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
uvicorn_logger = logging.getLogger('uvicorn.error')
logger.setLevel(uvicorn_logger.level)


app = FastAPI(title=cfg.APP_TITLE)

app.add_middleware(
    CORSMiddleware,
    allow_origins=cfg.ALLOWED_ORGINS,
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","DELETE"],
    allow_headers=["*"],
)

app.include_router(todo.router, prefix="/todo")
app.include_router(health.router, prefix="/health")