from fastapi import FastAPI
from src.task.controller import task_router

app = FastAPI()


app.include_router(task_router, prefix="/task", tags=["task"])

@app.get("/")
async def root():

    return {"message": "Hello World"}

