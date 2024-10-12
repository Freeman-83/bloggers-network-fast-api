from fastapi import APIRouter, Depends, HTTPException, Request

from sqlalchemy.orm import Session

from .schemas import GetTaskSchema, CreateTaskSchema

from .crud import get_task_from_db, create_task_to_db, get_tasks_list

from app.users.utils import get_user_from_token

from app.database import get_db


task_router = APIRouter()


@task_router.get('/tasks', response_model=list[GetTaskSchema])
def task_list(current_user: str = Depends(get_user_from_token),
              db: Session = Depends(get_db)):
    return get_tasks_list(db)


@task_router.post('/tasks', response_model=GetTaskSchema)
def create_task(request: Request,
                task: CreateTaskSchema,
                current_user: str = Depends(get_user_from_token),
                db: Session = Depends(get_db)):
    task.model_dump().update({'owner_id': current_user})
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
