import datetime

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from users.schemas import UserSchema, UserSchemaCreate
from users.models import User

from app.database import get_db

from users.crud import get_user_from_db, create_user_to_db

from .utils import create_jwt_token


user_router = APIRouter()


@user_router.post('/users', response_model=UserSchema)
def create_user(user: UserSchemaCreate, db: Session = Depends(get_db)):
    user = create_user_to_db(user=user, db=db)
    return user


@user_router.post('/login/')
async def login(user: User):
    for elem in db.users_data:
        if elem.username == user.username and elem.password == user.password:
            token = create_jwt_token({"sub": user.username})
            return {'access_token': token, "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid username or password")


@user_router.get('/users', response_model=list[UserSchema])
def users_list(db: Session = Depends(get_db)):
    


@user_router.get('/users/{task_id}', response_model=UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_from_db(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return user

