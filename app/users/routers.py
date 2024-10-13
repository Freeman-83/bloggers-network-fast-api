import datetime

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from users.schemas import GetUserSchema, CreateUserSchema

from app.database import get_db

from users.crud import (get_user_from_db,
                        create_new_user,
                        get_user_for_token_assignment,
                        get_users_list)

from .utils import create_jwt_token


user_router = APIRouter()


@user_router.post('/login')
def login(user: CreateUserSchema, db: Session = Depends(get_db)):
    current_user = get_user_for_token_assignment(user, db)
    if current_user:
        token = create_jwt_token({"sub": user.email})
        current_user.is_active = True
        db.add(current_user)
        db.commit()
        db.refresh(current_user)
        return {'access_token': token, "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid username or password")


@user_router.post('/logout')
def logout(user: CreateUserSchema, db: Session = Depends(get_db)):
    ...


@user_router.post('/users', response_model=GetUserSchema)
def create_user(user: CreateUserSchema, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user


@user_router.get('/users', response_model=list[GetUserSchema])
def users_list(db: Session = Depends(get_db)):
    return get_users_list(db)


@user_router.get('/users/{user_id}', response_model=GetUserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_from_db(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

