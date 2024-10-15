from fastapi import APIRouter, Depends, HTTPException, Request

from sqlalchemy.orm import Session

from app.utils import get_db

from .schemas import GetTaskSchema, CreateTaskSchema

from .crud import get_task_from_db, create_new_task, get_tasks_list

from app.users.utils import get_user_from_token
from app.users.crud import get_user_for_tasks_create


task_router = APIRouter()


@task_router.get('/tasks', response_model=list[GetTaskSchema])
async def task_list(current_user: str = Depends(get_user_from_token),
                    db: Session = Depends(get_db)):
    return get_tasks_list(db)


@task_router.post('/tasks', response_model=GetTaskSchema)
async def create_task(task: CreateTaskSchema,
                      current_user: str = Depends(get_user_from_token),
                      db: Session = Depends(get_db)):
    current_user_id = get_user_for_tasks_create(current_user, db)
    task.model_dump().update({'owner_id': current_user_id})
    return create_new_task(task=task, db=db)


@task_router.get('/tasks/{task_id}')
async def get_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task_from_db(task_id, db)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@task_router.patch('/tasks/{task_id}')
async def update_task(task_id):
    ...


@task_router.delete('/tasks/{task_id}')
async def delete_task(task_id):
    ...
