from datetime import date, time

from fastapi import APIRouter, Depends, HTTPException, Request

from sqlalchemy.orm import Session

from app.todo.models import Task
from app.todo.schemas import GetTaskSchema, CreateTaskSchema

from app.users.models import User
from app.users.dependences import get_user_from_token

from app.utils import get_db


task_router = APIRouter(prefix='/tasks')


@task_router.get('/', response_model=list[GetTaskSchema])
async def task_list(current_user: str = Depends(get_user_from_token),
                    db: Session = Depends(get_db)) -> list[Task]:
    task_list = db.query(Task).all()
    return task_list


@task_router.post('/', response_model=GetTaskSchema)
async def create_task(task: CreateTaskSchema,
                      request: Request,
                      current_user: str = Depends(get_user_from_token),
                      db: Session = Depends(get_db)):
    author_db = db.query(User).filter(User.email == current_user).first()
    task.author_id = author_db.id
    task_db = Task(**task.model_dump())
    db.add(task_db)
    db.commit()
    db.refresh(task_db)
    return task_db

@task_router.get('/{task_id}')
async def get_task(task_id: int,
                   current_user: str = Depends(get_user_from_token),
                   db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    return task


@task_router.patch('/{task_id}')
async def update_task(task_id):
    ...


@task_router.delete('/{task_id}')
async def delete_task(task_id):
    ...
