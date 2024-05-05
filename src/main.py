from fastapi import FastAPI
from src.task.controller import task_router
from src.upload.router import upload_router
from src.board.controller import board_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.include_router(task_router, prefix="/task", tags=["task"])
app.include_router(upload_router, prefix="/upload", tags=["upload"])
app.include_router(board_router, prefix="/board", tags=["board"])
app.add_middleware(CORSMiddleware, allow_origins=["*"])
@app.get("/")
async def root():

    return {"message": "Hello World"}

