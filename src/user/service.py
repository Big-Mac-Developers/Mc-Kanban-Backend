from database import get_db
import user.model as model
import json

USER_TABLE = "User"


def get_all_user():
    db =get_db()
    return db.table(USER_TABLE).select("*").execute()

def create_user(user: model.User):
    db = get_db()
    user_json = user.model_dump_json()
    user_dic = json.loads(user_json)
    data, count = db.table(USER_TABLE).insert(user_dic).execute()
    string, val = data
    return val[0]

def get_user(user: model.User):
    db = get_db()
    user =  db.table(USER_TABLE).select("*").eq('username', user.username).eq('password', user.password).execute()
    if user.data:
        return user.data
    else:
        print("No user found or error in execution")
        return None


