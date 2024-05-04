from src.database import get_db
from src.task.model import Maintask, Subtask
MAIN_TASK_TABLE = "Main_Task"
SUBTASK_TABLE = "Subtask"

def get_data():
    db =get_db()
    return db.table("Main_Task").select("*, Subtask (*)").execute()

def create_main_task(main_task: Maintask):
    db = get_db()
    db.table(MAIN_TASK_TABLE).insert(main_task).execute()

def create_sub_task(sub_task: Subtask):
    db = get_db()
    db.table(SUBTASK_TABLE).insert(sub_task).execute()

def get_main_task(id)->Maintask:
    db = get_db()
    data = db.table(MAIN_TASK_TABLE).select("*").execute()
    return data

