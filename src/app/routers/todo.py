from typing import Any, Optional
from uuid import UUID
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
import logging

from app.schemas import Todo, TodoCreate
from app.database import get_db
from app import crud


from app import models
from app.auth import authHelper
from app.schemas import User

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("", status_code=200, tags=["Todos"])
def read_todos(
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        completed: Optional[bool] = None,
        db: Session = Depends(get_db)
) -> Any:
    """
    Retrieve all todo items.
    """
    logger.debug("Retrieving all todo items")
    if completed is not None:
        todos = crud.Todo.get_by_completion(
            db, skip=skip, limit=limit, completed=completed)

    todos = crud.Todo.get_all(db, skip, limit)
    if todos:
        return todos
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@router.get("/{todo_id}", response_model=Todo, status_code=200, tags=["Todos"])
def read_todo(
    todo_id,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(authHelper.get_current_user)
) -> Any:
    todo = crud.Todo.get_single(db, todo_id)
    logger.debug(f"Retrieving todo {todo_id}")

    if not todo:
        logger.info(f"Todo item {todo_id} not found.")
        raise HTTPException(status_code=404, detail="Item not found")
    if not authHelper.get_current_user_superuser(
            current_user) and todo.owner_id != current_user.id:
        logger.info(
            f"{current_user.name} tried to access todo item {todo_id} with insufficient permissions")
        raise HTTPException(
            401,
            detail="Insufficient permissions to access todo item owned by another user")
    return todo


@router.post("", status_code=201, response_model=Todo, tags=["Todos"])
def create_todo(
    todo_in: TodoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        authHelper.get_current_user)):
    todo = crud.Todo.create(db, todo_in, user_id=current_user.id)
    logger.info(f"Created todo with ID of {todo.id}")

    return Todo(id=todo.id, title=todo.title,
                notes=todo.notes, completed=todo.completed, owner_id=current_user.id)


@router.put("/{todo_id}", status_code=200, tags=["Todos"])
def update_todo(todo_id, todo_in: Todo, db: Session = Depends(
        get_db), current_user: models.User = Depends(authHelper.get_current_user)) -> Any:
    todo = crud.Todo.get_single(db, todo_id)
    if not todo:
        logger.info(f"Todo item {todo_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")
    if not authHelper.get_current_user_superuser(
            current_user) and todo.owner_id != current_user.id:
        logger.info(
            f"{current_user.name} tried to access todo item {todo_id} with insufficient permissions")
        raise HTTPException(
            401,
            detail="Insufficient permissions to modify todo item owned by another user")

    todo = crud.Todo.update_todo(db, todo_in, todo_id)
    logger.debug(f"Updated todo item {todo_id}")
    return Todo(id=todo.id, title=todo.title,
                notes=todo.notes, completed=todo.completed, owner_id=current_user.id)


@router.delete("/{todo_id}", status_code=204, tags=["Todos"])
def delete_todo(todo_id, db: Session = Depends(
        get_db), current_user: models.User = Depends(authHelper.get_current_user)) -> Any:
    todo = crud.Todo.get_single(db, todo_id)

    if not todo:
        raise HTTPException(status_code=404, detail="Item not found")
    if not authHelper.get_current_user_superuser(
            current_user) and todo.owner_id != current_user.id:
        raise HTTPException(
            status_code=401,
            detail="Insufficient permissions to modify todo item owned by another user.")
    crud.Todo.delete(db, todo_id)
