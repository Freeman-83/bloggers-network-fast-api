from sqlalchemy.orm import Session

from app.database import SessionLocal

from todo.models import Task
from todo.schemas import TaskSchemaBase, TaskSchemaCreate, TaskSchema


def get_task_from_db(task_id, db: Session):
    return db.query(Task).filter(Task.id == task_id).first()


def create_task_to_db(task: TaskSchemaCreate, db: Session):
    task_db = Task(**task.model_dump())
    db.add(task_db)
    db.commit()
    db.refresh(task_db)
    return task_db
