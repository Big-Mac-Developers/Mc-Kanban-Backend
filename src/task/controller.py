from fastapi import APIRouter, Request
from src.task.service import create_main_task, get_main_task, create_sub_task
from src.task.model import Maintask_initial, Maintask, Subtask
task_router = APIRouter()
@task_router.post("/createMain")
async def create_main_task_route(request:Maintask_initial)-> Maintask:
    return create_main_task(main_task=request)

@task_router.post("/createSub")
async def create_sub_task_route(request:Subtask):
    return create_sub_task(request)
@task_router.get("main/{task_id}")
def get_main_task_route(task_id):
    return get_main_task(task_id)

@task_router.get("/{board_id}")
async def get_board_main_tasks_route(board_id):
    pass


