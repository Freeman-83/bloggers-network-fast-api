from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from todo.schemas import TaskSchemaBase #, CreateTaskSchema, GetTaskSchema
from todo.models import Task

from todo.crud import get_task, create_task

from app.database import SessionLocal, engine, get_db


Task.metadata.create_all(bind=engine)

task_router = APIRouter()


@task_router.get('/tasks', response_model=TaskSchemaBase)
async def task_list():
    ...


@task_router.post('/tasks', response_model=TaskSchemaBase)
async def create_task(task: TaskSchemaBase, db: Session = Depends(get_db)):
    return create_task(db=db, task=task)


@task_router.get('/tasks/{task_id}')
async def get_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task(task_id, db)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@task_router.put('/tasks/{task_id}')
def update_task(task_id):
    ...


@task_router.delete('/tasks/{task_id}')
def delete_task(task_id):
    ...
