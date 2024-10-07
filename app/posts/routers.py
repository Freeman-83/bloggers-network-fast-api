from fastapi import APIRouter

from .schemas import PostBase

post_router = APIRouter()


@post_router.get('/posts', response_model=PostBase)
async def post_list():
    
    ...


@post_router.post('/posts', response_model=PostBase)
async def create_post(post: PostBase):
    return post


@post_router.get('/posts/{post_id}')
async def get_post(post_id, post: PostBase):
    return post


@post_router.put('/posts/{post_id}')
def update_post(post_id):
    ...


@post_router.delete('/posts/{post_id}')
def update_post(post_id):
    ...
