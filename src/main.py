from fastapi import FastAPI
from user.controller import user_router
# from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(user_router, prefix="/user")
# app.include_router(task_router, prefix="/task", tags=["task"])
# app.add_middleware(CORSMiddleware, allow_origins=["*"])
@app.get("/")
async def root():

    return {"message": "Hello World"}

