import uvicorn

import sys
sys.path.append(".")

from fastapi import FastAPI

from pathlib import Path

from users.routers import user_router
from posts.routers import post_router


app = FastAPI()


app.include_router(user_router)
app.include_router(post_router)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
