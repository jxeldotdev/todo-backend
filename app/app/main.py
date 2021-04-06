import app.models
from typing import Optional

from fastapi import Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
from uuid import UUID

from app import crud, models, schemas
from app.database import SessionLocal, engine
from app.routers import todo

# Create tables on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo Rest API"
)

app.include_router(todo.router)