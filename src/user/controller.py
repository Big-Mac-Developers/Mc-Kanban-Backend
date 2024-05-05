from fastapi import APIRouter, Request
import user.model as model

user_router = APIRouter()

@user_router.post("/Users/")
async def create_user_route(User:model.User):
    return User
