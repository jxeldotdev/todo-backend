from sqlalchemy.sql.operators import json_getitem_op
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from starlette.requests import HTTPConnection
from fastapi.encoders import jsonable_encoder

from app.schemas import Todo, TodoDelete
from app.database import get_db
from app import crud

router = APIRouter()


@router.get("/todo", response_model=List[Todo], tags=["Todos"])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip, limit)
    todos_json = jsonable_encoder(todos)

    if not todos:
        raise HTTPException(status_code=404)

    return todos_json



@router.get("/todo/{todo_id}", response_model=Todo, tags=["Todos"])
def read_todo(todo_id: UUID, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)

    if todo:
        todo = jsonable_encoder(todo)
        return todo
    else:
        raise HTTPException(status_code=404)


@router.post("/todo", response_model=Todo, tags=["Todos"])
def create_todo(todo_in: Todo, db: Session = Depends(get_db)):

    todo = crud.create_todo(db, todo_in)
    if todo:
        todo = jsonable_encoder(todo)        
        return todo



@router.put("/todo/{todo_id}", response_model=Todo, tags=["Todos"])
def update_todo(todo_id, todo_in: Todo, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)

    if not todo:
        raise HTTPException(status_code=404)

    item = crud.update_todo(db, todo_in, todo_id)
    item = jsonable_encoder(item)
    print(item)
    return item
    


@router.delete("/todo/{todo_id}", response_model=TodoDelete, tags=["Todos"])
def delete_todo(todo_id, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)

    if not todo:
        raise HTTPException(status_code=404)

    crud.delete_todo(db, todo_id)
    return HTTPException(status_code=201)