from pydantic import BaseModel, EmailStr

from app.todo.models import Task


class UserSchemaBase(BaseModel):

    username: str
    email: EmailStr


class UserSchemaCreate(UserSchemaBase):

    password: str


class UserSchema(UserSchemaBase):

    id: int
    tasks: list[Task] = []

    class Config:
        orm_mode = True