from src.database import get_db
import src.user.model as model
import json

USER_TABLE = "User"


def get_data():
    db =get_db()
    return db.table("User").select("*").execute()

