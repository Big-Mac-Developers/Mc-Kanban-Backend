from fastapi import APIRouter, Request
from src.task.service import create_main_task, get_main_task, create_sub_task, update_subtask_status,update_subtask,delete_subtask
from src.task.model import Maintask_initial, Maintask, Subtask, Subtask_initial,TaskStatus
task_router = APIRouter()
@task_router.post("/createMain")
async def create_main_task_route(request:Maintask_initial)-> Maintask:
    return create_main_task(main_task=request)

@task_router.post("/createSub")
async def create_sub_task_route(request:Subtask_initial):
    return create_sub_task(request)
@task_router.get("main/{task_id}")
def get_main_task_route(task_id):
    return get_main_task(task_id)

@task_router.get("/{board_id}")
async def get_board_main_tasks_route(board_id):
    pass

@task_router.patch("/updateSub/{task_id}")
async def update_subtask_status_route(subtask_id, status:TaskStatus):
    return update_subtask_status(subtask_id, status)
@task_router.patch("/updateSub")
async def update_subtask_route(req:Subtask):
    return update_subtask(req)

@task_router.delete("/deleteSub/{task_id}")
async def delete_subtask_status_route(subtask_id):
    return delete_subtask(subtask_id)


