from src.database import get_db
from src.task.model import Maintask, Subtask, Subtask_initial, TaskStatus
import json
MAIN_TASK_TABLE = "Main_Task"
SUBTASK_TABLE = "Subtask"

def get_data():
    db =get_db()
    return db.table("Main_Task").select("*, Subtask (*)").execute()

def create_main_task(main_task: Maintask):
    db = get_db()
    db.table(MAIN_TASK_TABLE).insert(main_task).execute()

def create_sub_task(sub_task: Subtask_initial):
    db = get_db()
    sub_task_json = sub_task.model_dump_json()
    sub_task_dic = json.loads(sub_task_json)


    data, count = db.table(SUBTASK_TABLE).insert(sub_task_dic).execute()
    string, val = data
    return val[0]

def get_main_task(id)->Maintask:
    db = get_db()
    data = db.table(MAIN_TASK_TABLE).select("*").execute()
    return data

def update_subtask_status(subtask_id, status:TaskStatus ):
    db = get_db()
    print(status.value)
    data, count = db.table(SUBTASK_TABLE).update({"status": status.value}).eq("id", subtask_id).execute()
    string, val = data
    return val[0]

def update_subtask(subtask:Subtask):
    ##to do fix uuid
    db = get_db()
    subtask_json = subtask.model_dump_json()
    subtask_dic = json.loads(subtask_json)
    data, count = db.table(SUBTASK_TABLE).update(subtask_dic).eq("id", subtask.id).execute()
    string, val = data
    print(val)
    return val

def delete_subtask(subtask_id):
    db = get_db()
    data, count = db.table(SUBTASK_TABLE).delete().where("id", subtask_id).execute()
    return count