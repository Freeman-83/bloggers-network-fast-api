from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database import SessionLocal, engine

from todo.schemas import TaskSchema, TaskSchemaCreate
from todo.models import Task

from todo.crud import get_task_from_db, create_task_to_db

from app.database import get_db

task_router = APIRouter()


@task_router.get('/tasks', response_model=TaskSchema)
def task_list():
    ...


@task_router.post('/tasks', response_model=TaskSchema)
def create_task(task: TaskSchemaCreate, db: Session = Depends(get_db)):
    return create_task_to_db(db=db, task=task)


@task_router.get('/tasks/{task_id}')
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task_from_db(task_id, db)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@task_router.put('/tasks/{task_id}')
def update_task(task_id):
    ...


@task_router.delete('/tasks/{task_id}')
def delete_task(task_id):
    ...
