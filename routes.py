from fastapi import APIRouter
from ai_handler import fetch_ai_response

router = APIRouter()

# @router.post("/chat/")
# async def chat_endpoint(user_input: dict):
#     prompt = user_input.get("prompt", "")
#     ai_response = await fetch_ai_response(prompt)
#     return {"response": ai_response}

@app.post("/chat/")
async def chat_endpoint(req: Request):
    body = await req.json()
    prompt = body.get("prompt", "")
    history = body.get("history", [])
    name = body.get("name")
    level = body.get("level")
    major = body.get("major")
    year = body.get("year")
    career_goal = body.get("careerGoal")

    ai_response = await fetch_ai_response(
        history=history,
        prompt=prompt,
        name=name,
        level=level,
        major=major,
        year=year,
        career_goal=career_goal
    )
    return {"response": ai_respons
