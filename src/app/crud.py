import logging

from sqlalchemy.exc import SQLAlchemyError
import sqlalchemy
from sqlalchemy.orm import Session, clear_mappers
import uuid

from app import models
from app import schemas

logger = logging.getLogger(__name__)


#TODO: Add logging in each functionß
class Todo:

    def get_single(db: Session, todo_id: uuid.uuid4):
        """
        Return Todo Item by UUID
        """
        return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

    def get_all(db: Session, skip, limit):
        """
        Returns all Todo Items
        """
        return db.query(models.Todo).offset(skip).limit(limit).all()

    def get_by_completion(db: Session, skip, limit, completed):
        """
        Return todo items by completion status
        """
        todos = db.query(
            models.Todo).filter(
            models.Todo.completed == completed).all()
        if todos:
            return todos

    def create(db: Session, todo: schemas.TodoCreate):
        """
        Create a Todo Item
        """
        db_todo = models.Todo(
            title=todo.title,
            notes=todo.notes,
            completed=todo.completed)
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo

    def delete(db: Session, todo_id: uuid.UUID):
        """
        Delete a Todo Item by UUID
        """
        db_todo = db.query(
            models.Todo).filter(
            models.Todo.id == todo_id).first()
        if db_todo:
            db.delete(db_todo)
            db.commit()

    def update_todo(db: Session, todo: schemas.Todo, todo_id: uuid.UUID):
        """
        Update an existing todo item or create oneo[]
        """

        db_todo = db.query(
            models.Todo).filter(
            models.Todo.id == todo.id).first()

        if not db_todo:
            raise sqlalchemy.exc.NoSuchColumnError
        else:
            db_todo.title = todo.title
            db_todo.notes = todo.notes
            db_todo.completed = todo.completed
            db.commit()

        return db_todo
