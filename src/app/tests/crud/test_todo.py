from sqlalchemy.orm import Session

from app import crud
from app.database import SessionLocal
from app.schemas import Todo, TodoCreate, TodoDelete

import uuid
import typing
from pytest import raises

def test_create_item(db: Session) -> None:
    title = "Example Item 1"
    notes = "Example Notes"
    todo_item = TodoCreate(title=title, notes=notes)
    todo = crud.Todo.create(db, todo_item)
    assert todo.title == title
    assert todo.notes == notes
    assert todo.completed == False
    assert type(todo.id) == uuid.UUID


def test_get_todo(db: Session) -> None:
    title = "Example Item 1"
    notes = "Example Notes"
    todo_item = TodoCreate(title=title, notes=notes)
    todo = crud.Todo.create(db, todo_item)
    db_todo = crud.Todo.get_single(db, todo.id)

    assert db_todo
    assert db_todo.title == title
    assert db_todo.notes == notes
    assert db_todo.completed == False


def test_get_all_todo_single(db: Session) -> None:
    title = "Example Item 1"
    notes = "Example Notes"
    todo_item = TodoCreate(title=title, notes=notes)
    todo_item = TodoCreate(title=title, notes=notes)
    todo = crud.Todo.create(db, todo_item)
    todo2 = crud.Todo.create(db, todo_item)
    db_todos = crud.Todo.get_all(db, skip=0, limit=100)

    assert db_todos
    assert type(db_todos) == list
    assert type(db_todos[0].id) == uuid.UUID
    assert db_todos[0]
    assert db_todos[0].completed == todo.completed
    assert db_todos[0].notes == todo.notes
    assert db_todos[0].title == todo.title
    assert db_todos[1].completed == todo2.completed
    assert db_todos[1].notes == todo2.notes
    assert db_todos[1].title == todo2.title
    assert len(db_todos) > 1



def test_complete_todo(db: Session) -> None:
    title = "Example Item 1"
    notes = "Example Notes"
    todo_item = TodoCreate(title=title, notes=notes)
    todo = crud.Todo.create(db, todo_item)
    todo2 = Todo(id=todo.id, title=title, notes=notes, completed=True)
    todo_update = crud.Todo.update_todo(db, todo=todo2, todo_id=todo.id)

    assert todo_update
    assert todo_update.id == todo.id
    assert todo.title == todo.title
    assert todo.notes == todo2.notes
    assert todo.completed == todo2.completed


def test_update_todo_description(db: Session) -> None:
    title = "Example Item 1"
    notes = "Example Notes"

    todo_item = TodoCreate(title=title, notes=notes)
    todo = crud.Todo.create(db, todo_item)

    notes2 = "Updated notes"
    todo2 = Todo(id=todo.id, title=title, notes=notes2)
    todo_update = crud.Todo.update_todo(db, todo=todo2, todo_id=todo.id)

    assert todo.id == todo_update.id
    assert todo.title == todo2.title
    assert todo_update.notes == notes2
    assert todo_update.completed == False


def test_delete_todo(db: Session) -> None:
    title = "Example Item 1"
    notes = "Example Notes"
    todo_in = TodoCreate(title=title, notes=notes)
    todo = crud.Todo.create(db, todo_in)
    todo2 = crud.Todo.delete(db, todo.id)
    todo3 = crud.Todo.get_single(db, todo_id=todo.id)

    assert todo3 is None
