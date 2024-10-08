import config

import uvicorn

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from users.routers import user_router
from todo.routers import task_router


app = FastAPI()


app.include_router(user_router)
app.include_router(task_router)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
