from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):

    id: int
    username: str
    email: EmailStr


class UserCreate(UserBase):

    password: str