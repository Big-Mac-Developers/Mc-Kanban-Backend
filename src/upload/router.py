from fastapi import APIRouter, Request, File,Form, UploadFile
from pypdf import PdfReader
import io
from src.ai.ai import extract_tasks_from_text

upload_router = APIRouter()

@upload_router.post("/")
async def upload_file(request: Request,
                      file: UploadFile= File(None),

                      ):
    file_content = await file.read()
    stream = io.BytesIO(file_content)

    reader = PdfReader(stream)
    number_of_pages = len(reader.pages)
    text = ''.join([page.extract_text() for page in reader.pages])
    response = extract_tasks_from_text(text)

    return response