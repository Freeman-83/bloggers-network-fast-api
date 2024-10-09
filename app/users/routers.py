from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from users.schemas import UserSchema, UserSchemaCreate

from app.database import get_db

from users.crud import get_user_from_db, create_user_to_db


user_router = APIRouter()


@user_router.post('/users', response_model=UserSchema)
def create_user(user: UserSchemaCreate, db: Session = Depends(get_db)):
    user = create_user_to_db(user=user, db=db)
    return user


@user_router.get('/users/{task_id}', response_model=UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_from_db(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return user

