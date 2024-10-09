import config
import uvicorn

from fastapi import FastAPI
from sqlalchemy.orm import Session

from database import engine

import todo, users

from users.routers import user_router
from todo.routers import task_router


app = FastAPI()


app.include_router(user_router)
app.include_router(task_router)

todo.models.Base.metadata.create_all(bind=engine)
users.models.Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
