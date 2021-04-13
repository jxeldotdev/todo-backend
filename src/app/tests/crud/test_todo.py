from pydantic.fields import T
from sqlalchemy.orm import Session

from app import crud
from app.schemas import Todo, TodoCreate, TodoDelete

import uuid

def test_create_item(db: Session) -> None:
    title = "Example Item 1"
    notes = "Example Notes"
    todo_item = TodoCreate(title=title, notes=notes)
    todo = crud.Todo.create(todo_item)
    assert todo.title == title
    assert todo.notes == notes
    assert todo.completed == False
    assert type(todo.id) == uuid.UUID


def test_get_todo(db: Session) -> None:
    title = "Example Item 1"
    notes = "Example Notes"
    todo_item = TodoCreate(title=title, notes=notes)
    todo = crud.Todo.create(db, todo_item)
    db_todo = crud.Todo.get_single(db=db, todo_id=todo.id)
    
    assert db_todo
    assert db_todo.title == title
    assert db_todo.notes == notes
    assert db_todo.completed == False


def test_complete_todo(db: Session) -> None:
    title = "Example Item 1"
    notes = "Example Notes"
    todo_item = TodoCreate(title=title, notes=notes)
    todo = crud.Todo.create(db, todo_item)
    todo2 = Todo(id=todo.id, title=title, notes=notes, completed=True)
    todo_update = crud.Todo.update_todo(db, todo2)

    assert todo2.id == todo.id
    assert todo.title == todo.title
    assert todo.notes == todo2.notes
    assert todo.completed == todo2.completed


def test__item(db: Session) -> None:
    title = "Example Item 1"
    notes = "Example Notes"
    todo_item = TodoCreate(title=title, notes=notes)
    todo = crud.Todo.create(todo_item)
    assert todo.title == title
    assert todo.notes == notes
    assert todo.completed == False
