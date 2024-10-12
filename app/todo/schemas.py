from pydantic import BaseModel, ConfigDict


class TaskSchemaBase(BaseModel):
    title: str
    description: str | None = None


class CreateTaskSchema(TaskSchemaBase):
    pass


class GetTaskSchema(TaskSchemaBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

    

