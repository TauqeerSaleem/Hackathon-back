from fastapi import FastAPI
from ai_handler import fetch_ai_response
import asyncio

app = FastAPI()

@app.post("/chat/")
async def chat_endpoint(user_input: dict):
    prompt = user_input.get("prompt", "")
    ai_response = await fetch_ai_response(prompt)
    return {"response": ai_response}