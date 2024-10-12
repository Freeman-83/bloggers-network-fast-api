from sqlalchemy.orm import Session

from app.database import SessionLocal

from todo.models import Task
from todo.schemas import CreateTaskSchema


def get_task_from_db(task_id, db: Session):
    return db.query(Task).filter(Task.id == task_id).first()

def get_tasks_list(db: Session):
    return db.query(Task).all()

def create_task_to_db(task: CreateTaskSchema, db: Session):
    task_db = Task(**task.model_dump())
    db.add(task_db)
    db.commit()
    db.refresh(task_db)
    return task_db
