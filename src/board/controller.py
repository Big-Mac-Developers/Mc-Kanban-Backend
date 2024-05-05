from fastapi import APIRouter, Request
from src.board.model import BoardInitial
board_router = APIRouter()

@board_router.post("/create")
async def create_main_task_route(request, board:BoardInitial):

    return "hi"