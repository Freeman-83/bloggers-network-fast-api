from pydantic import BaseModel, ConfigDict


class TaskSchemaBase(BaseModel):

    model_config = ConfigDict(from_attributes = True)

    title: str
    description: str

        


# class CreateTaskSchema(TaskSchemaBase):

#     ...


# class TaskSchema(TaskSchemaBase):

#     id: int
#     completed: bool = False

#     class Config:
#         from_attributes = True

    

