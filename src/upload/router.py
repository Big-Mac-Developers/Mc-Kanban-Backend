from fastapi import APIRouter, Request, File, UploadFile

upload_router = APIRouter()
@upload_router.post("/upload")
async def upload_file(request:Request, uploadFile:UploadFile):
    file_content = await uploadFile.read()
    return {"filename": uploadFile.filename, "content": file_content}