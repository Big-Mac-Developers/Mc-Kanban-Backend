from fastapi import APIRouter, Request
import user.model as model
import user.service as service
user_router = APIRouter()

@user_router.post("/Users/")
async def create_user_route(User:model.User):
    created_user = service.create_user(User)
    return created_user

@user_router.post("/Users/getUser")
async def get_user_route(User:model.User):
    return service.get_user(User)