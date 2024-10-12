from pydantic import BaseModel, EmailStr, ConfigDict

from app.todo.schemas import GetTaskSchema


class UserSchemaBase(BaseModel):
    email: EmailStr


class CreateUserSchema(UserSchemaBase):
    password: str


class GetUserSchema(UserSchemaBase):
    id: int
    is_active: bool
    tasks: list[GetTaskSchema] = []

    class Config:
        from_attributes = True
