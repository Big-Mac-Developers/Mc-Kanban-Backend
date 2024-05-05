from pydantic import BaseModel
from uuid import UUID


class User(BaseModel):
    username: str
    password: str

