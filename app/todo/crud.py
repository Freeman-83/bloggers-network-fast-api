from sqlalchemy.orm import Session

from todo.models import Task
from todo.schemas import TaskSchemaBase #, CreateTaskSchema, GetTaskSchema


def get_task(task_id, db: Session):
    return db.query(Task).filter(Task.id == task_id).first()


def create_task(task: TaskSchemaBase, db: Session,):
    task_db = Task(**task.model_dump())
    db.add(task_db)
    db.commit()
    db.refresh(task_db)
    return task_db