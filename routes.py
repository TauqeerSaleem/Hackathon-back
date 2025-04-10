from fastapi import APIRouter, Request
from ai_handler import fetch_ai_response

router = APIRouter()

@router.post("/chat/")
async def chat_endpoint(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "")
    history = body.get("history", [])
    response = await fetch_ai_response(prompt, history)
    return {"response": response}