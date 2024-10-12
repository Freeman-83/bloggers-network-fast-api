from sqlalchemy.orm import Session

from users.models import User
from users.schemas import CreateUserSchema


def get_user_from_db(user_id, db: Session):
    return db.query(User).filter(User.id == user_id).first()

def get_users_list(db: Session):
    return db.query(User).all()

def create_new_user(user: CreateUserSchema, db: Session):
    user_db = User(**user.model_dump())
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

def get_user_for_token_assignment(current_user, db: Session):
    return db.query(User).filter(
        User.email == current_user.email,
        User.password == current_user.password
    ).first()
