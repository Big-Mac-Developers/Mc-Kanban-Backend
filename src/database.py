from supabase import create_client, Client
from dotenv import dotenv_values


config = dotenv_values(".env")
url = config["SUPABASE_URL"]
key = config["SUPABASE_KEY"]

client = create_client(url, key)


def get_db() -> Client:
    return client