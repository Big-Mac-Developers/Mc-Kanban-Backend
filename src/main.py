from fastapi import FastAPI
from src.task.controller import task_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.include_router(task_router, prefix="/task", tags=["task"])
app.add_middleware(CORSMiddleware, allow_origins=["*"])
@app.get("/")
async def root():

    return {"message": "Hello World"}

