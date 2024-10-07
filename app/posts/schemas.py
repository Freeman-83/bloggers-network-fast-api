from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):

    model_config = ConfigDict(orm_mode = True)

    id: int
    description: str
    text: str
