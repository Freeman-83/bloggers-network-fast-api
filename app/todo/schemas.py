from datetime import date, time
from pydantic import BaseModel, ConfigDict


class TaskSchemaBase(BaseModel):
    title: str


class CreateTaskSchema(TaskSchemaBase):
    author_id: int | None = None
    complete_date: date
    complete_time: time


class GetTaskSchema(TaskSchemaBase):
    id: int
    author_id: int
    complete_date: date
    complete_time: time

    class Config:
        from_attributes = True
