from fastapi import APIRouter
from ai_handler import fetch_ai_response

router = APIRouter()

@router.post("/chat/")
async def chat_endpoint(user_input: dict):
    prompt = user_input.get("prompt", "")
    ai_response = await fetch_ai_response(prompt)
    return {"response": ai_response}
