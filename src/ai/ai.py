from fastapi import FastAPI
import os
from anthropic import Anthropic
from dotenv import load_dotenv
from pypdf import PdfReader
import json
import re

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


def ask_question(model, prompt, client):
    message = client.messages.create(
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="claude-3-opus-20240229",
    )
    return message.content[0].text

def summaries_task(model, client, respone):
    query = f"""estimate the diffculty of each task from 1 (low) to 10 (high)and convert the all tasks {respone} into this structure 

    """ 

    return ask_question(model, query, client)
     
def read_pdf(file_path):
    reader = PdfReader(file_path)
    number_of_pages = len(reader.pages)
    text = ''.join([page.extract_text() for page in reader.pages])
    return text

def extract_tasks_from_text(text):
    load_dotenv()
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    client = Anthropic(
        # This is the default and can be omitted
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
    )
    model = "claude-3-opus-20240229"
    prompt =  f"""Here is an assignment paper: <paper>{text}</paper> what is the key tasks for this assignment? """
    respone = ask_question(model, prompt, client)
    json = summaries_task(model, client, respone)
    return json
def main():

    load_dotenv()
    api_key = os.environ.get("ANTHROPIC_API_KEY")


    client = Anthropic(
        # This is the default and can be omitted
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
    )

    file = read_pdf('src\Project Management Part 2-Mind Map and Project Management 28032024 .pdf')
    model="claude-3-opus-20240229"
    prompt =  f"""Here is an assignment paper: <paper>{file}</paper> what is the key tasks for this assignment? """
    respone = ask_question(model, prompt, client)
    json = summaries_task(model, client, respone)


if  __name__ == '__main__':
    main()