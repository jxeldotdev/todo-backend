from fastapi.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.functions import mode
from app.database import SQLALCHEMY_DATABASE_URL
import sqlalchemy
from sqlalchemy.orm import Session
import uuid

from app import models, schemas

# Todo Items

def get_todo(db: Session, todo_id: uuid.uuid4):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()



def get_todos(db: Session, skip, limit):
    return db.query(models.Todo).offset(skip).limit(limit).all()



def get_todos_by_completion(db: Session, completed: bool):
    todos = db.query(
        models.Todo).filter(
        models.Todo.completed == completed).first()
    if todos:
        return todos


def create_todo(db: Session, todo: schemas.Todo):
    db_todo = models.Todo(title=todo.title, notes=todo.notes, completed=False)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: uuid.UUID):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()

def update_todo(db: Session, todo: schemas.Todo, todo_id: uuid.UUID):
    # check if it exists
    
    db_todo = db.query(models.Todo).filter(
        models.Todo.completed == todo.completed,
        models.Todo.id == todo.id,
        models.Todo.title == todo.title,
        models.Todo.notes == todo.notes
    ).first()

    if not db_todo:
        return HTTPException(status_code=404)
    
    db_todo.title = todo.title
    db_todo.notes = todo.notes
    db_todo.completed = todo.completed

    db.commit()
    db.refresh()


    return db_todo

