from sqlalchemy.sql.operators import json_getitem_op
from typing import Any
from uuid import UUID
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.schemas import Todo, TodoCreate, TodoDelete
from app.database import get_db
from app import crud

router = APIRouter()


@router.get("/todo", status_code=200, tags=["Todos"])
def read_todos(
    skip: int = 0, 
    limit: int = 100,
     db: Session = Depends(get_db)
) -> Any:
    """
    Retrieve all todo items.
    """
    todos = crud.Todo.get_all(db, skip, limit)
    return todos



@router.get("/todo/{todo_id}", response_model=Todo, status_code=200, tags=["Todos"])
def read_todo(
    todo_id: UUID,
     db: Session = Depends(get_db)
) -> Any:
    todo = crud.Todo.get_single(db, todo_id)

    if todo:
        return todo
    else:
        raise HTTPException(status_code=404)


@router.post("/todo", status_code=201, tags=["Todos"])
def create_todo(todo_in: TodoCreate, db: Session = Depends(get_db)):
    return crud.Todo.create(db, todo_in)




@router.put("/todo/{todo_id}", status_code=204, tags=["Todos"])
def update_todo(todo_id, todo_in: Todo, db: Session = Depends(get_db)) -> Any:
    
    if not crud.Todo.get_single(db, todo_id):
        raise HTTPException(status_code=404, detail="Item not found")

    todo = crud.Todo.update_todo(db, todo_in, todo_id)


@router.delete("/todo/{todo_id}", status_code=204, tags=["Todos"])
def delete_todo(todo_id, db: Session = Depends(get_db)) -> Any:
    todo = crud.Todo.get_single(db, todo_id)

    if not todo:
        raise HTTPException(status_code=404)

    crud.Todo.delete_todo(db, todo_id)