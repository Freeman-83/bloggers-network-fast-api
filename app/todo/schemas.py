from pydantic import BaseModel, ConfigDict


class TaskSchemaBase(BaseModel):

    model_config = ConfigDict(from_attributes = True)

    title: str
    description: str

        


class TaskSchemaCreate(TaskSchemaBase):

    ...


class TaskSchema(TaskSchemaBase):

    model_config = ConfigDict(from_attributes = True)

    id: int
    completed: bool = False

    

