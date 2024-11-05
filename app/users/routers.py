import datetime

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.users.schemas import GetUserSchema, CreateUserSchema

from app.utils import get_db

from app.users.models import User

from app.users.dependences import create_jwt_token

from app.exceptions import LoginErrorException, custom_exception_handler


user_router = APIRouter(prefix='/users')


@user_router.post('/login')
async def login(user: CreateUserSchema, db: Session = Depends(get_db)):
    current_user = db.query(User).filter(
        User.email == user.email,
        User.password == user.password
    ).first()

    if current_user:
        token = create_jwt_token({'sub': current_user.email})
        current_user.is_active = True
        db.add(current_user)
        db.commit()
        db.refresh(current_user)
        return {'access_token': token, 'token_type': 'bearer'}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail='Invalid username or password')


@user_router.post('/logout')
async def logout(user: CreateUserSchema, db: Session = Depends(get_db)):
    ...


@user_router.post('/', response_model=GetUserSchema)
async def create_user(user: CreateUserSchema, db: Session = Depends(get_db)):
    user_db = User(**user.model_dump())
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db


@user_router.get('/', response_model=list[GetUserSchema])
async def users_list(db: Session = Depends(get_db)) -> list[User]:
    users_list = db.query(User).all()
    return users_list


@user_router.get('/{user_id}', response_model=GetUserSchema)
async def get_user(user_id: int, db: Session = Depends(get_db)) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user

