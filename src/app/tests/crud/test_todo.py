from datetime import datetime
from sqlalchemy.orm import Session

from app import crud
from app.schemas import Todo, TodoCreate
from app.tests.utils import utils

import uuid


def test_create_item(db: Session) -> None:

    utils.recreate()

    title = "Example Item 1"
    notes = "Example Notes"
    todo_item = TodoCreate(title=title, notes=notes)
    todo = crud.Todo.create(db, todo_item)
    assert todo.title == title
    assert todo.notes == notes
    assert todo.completed is False
    assert isinstance(todo.id, int)


def test_get_todo(db: Session) -> None:

    title = "Example Item 1"
    notes = "Example Notes"
    todo_item = TodoCreate(title=title, notes=notes)
    todo = crud.Todo.create(db, todo_item)
    db_todo = crud.Todo.get_single(db, todo.id)

    assert db_todo
    assert db_todo.title == title
    assert db_todo.notes == notes
    assert isinstance(db_todo.created_at, datetime)
    assert db_todo.completed is False


def test_get_incompleted_todos(db: Session) -> None:

    title = "Example Item 2"
    notes = "Example Notes 2"
    todo_item = TodoCreate(title=title, notes=notes)
    todo = crud.Todo.create(db, todo_item)

    db_todo = crud.Todo.get_by_completion(db, completed=False, skip=0, limit=10)

    assert db_todo
    for todo in db_todo:
        assert todo.completed is False


def test_get_completed_todos(db: Session) -> None:

    title = "Example Item 3"
    notes = "Example Notes 3"

    todo_item = TodoCreate(title=title, notes=notes, completed=True)
    todo = crud.Todo.create(db, todo_item)
    db_todo = crud.Todo.get_by_completion(db, completed=True, skip=0, limit=10)

    assert db_todo
    for todo in db_todo:
        assert todo.completed


def test_complete_todo(db: Session) -> None:
    title = "Example Item 1"
    notes = "Example Notes"
    todo_item = TodoCreate(title=title, notes=notes)
    todo = crud.Todo.create(db, todo_item)
    todo2 = Todo(id=todo.id, title=title, notes=notes, completed=True, created_at=todo.created_at)
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
    todo2 = Todo(id=todo.id, title=title, notes=notes2, created_at=todo.created_at)
    todo_update = crud.Todo.update_todo(db, todo=todo2, todo_id=todo.id)


    assert todo.id == todo_update.id
    assert todo.title == todo2.title
    assert todo_update.notes == notes2
    assert todo_update.completed is False


def test_delete_todo(db: Session) -> None:
    title = "Example Item 1"
    notes = "Example Notes"
    todo_in = TodoCreate(title=title, notes=notes)
    todo = crud.Todo.create(db, todo_in)
    todo2 = crud.Todo.delete(db, todo.id)
    todo3 = crud.Todo.get_single(db, todo_id=todo.id)

    assert todo3 is None
