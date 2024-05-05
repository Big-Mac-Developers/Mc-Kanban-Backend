from pydantic import BaseModel
class BoardInitial(BaseModel):
    title: str
    description: str
