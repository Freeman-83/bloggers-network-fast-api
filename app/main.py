import config
import uvicorn

from fastapi import FastAPI

from database import engine

from todo import models as tasks_models
from users import models as users_models

from todo.routers import task_router
from users.routers import user_router


app = FastAPI()


app.include_router(task_router)
app.include_router(user_router)

tasks_models.Base.metadata.create_all(bind=engine)
users_models.Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
