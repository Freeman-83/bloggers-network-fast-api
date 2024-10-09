from pydantic import BaseModel, EmailStr, ConfigDict

from app.todo.schemas import TaskSchema


class UserBase(BaseModel):
    email: str


class UserSchemaCreate(UserBase):
    password: str


class UserSchema(UserBase):
    id: int
    is_active: bool
    tasks: list[TaskSchema] = []

    class Config:
        from_attributes = True
