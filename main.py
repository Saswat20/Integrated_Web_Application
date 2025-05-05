from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class Message(BaseModel):
    user_input: str

@app.post("/chat")
async def chat(msg: Message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": msg.user_input}]
    )
    return {"response": response['choices'][0]['message']['content']}