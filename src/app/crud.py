import logging
import sqlalchemy
from sqlalchemy.orm import Session

from app import models, schemas

logger = logging.getLogger(__name__)

# TODO: Add logging in each function


class Todo:
    def get_single(db: Session, todo_id: int):
        """
        Return Todo Item by ID
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
        todos = db.query(models.Todo).filter(
            models.Todo.completed == completed).all()
        if todos:
            return todos

    def create(db: Session, todo: schemas.TodoCreate):
        """
        Create a Todo Item
        """
        db_todo = models.Todo(**todo.dict())
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo

    def delete(db: Session, todo_id: int):
        """
        Delete a Todo Item by UUID
        """
        db_todo = db.query(models.Todo).filter(
            models.Todo.id == todo_id).first()
        if db_todo:
            db.delete(db_todo)
            db.commit()

    def update_todo(db: Session, todo: schemas.Todo, todo_id: int):
        """
        Update an existing todo item or create one
        """

        db_todo = db.query(models.Todo).filter(
            models.Todo.id == todo.id).first()

        if not db_todo:
            raise sqlalchemy.exc.NoSuchColumnError
        else:
            db_todo.title = todo.title
            db_todo.notes = todo.notes
            db_todo.completed = todo.completed
            try:
                if todo.created_at:
                    db_todo.created_at = todo.created_at    
            except AttributeError:
                # Only will happen when updating a todo item since we don't need to update created_at..
                pass
            db_todo
            db.commit()

        return db_todo
