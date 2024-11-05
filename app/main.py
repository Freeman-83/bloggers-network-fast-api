import config
import uvicorn

from fastapi import FastAPI

from database import engine

from app.todo import models as tasks_models
from app.users import models as users_models

from app.todo.routers import task_router
from app.users.routers import user_router


app = FastAPI(root_path='/api')


app.include_router(task_router)
app.include_router(user_router)

tasks_models.Base.metadata.create_all(bind=engine)
users_models.Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
