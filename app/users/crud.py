from sqlalchemy.orm import Session

from app.database import SessionLocal

from users.models import User
from users.schemas import UserSchemaCreate


def get_user_from_db(user_id, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def create_user_to_db(user: UserSchemaCreate, db: Session):
    user_db = User(**user.model_dump())
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db
