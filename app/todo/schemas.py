from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    title: str
    description: str | None = None


class TaskSchemaCreate(TaskBase):
    pass


class TaskSchema(TaskBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

    

