from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai_handler import fetch_ai_response

app = FastAPI()

# Add this middleware to handle CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL (Next.js default port)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat/")
async def chat_endpoint(user_input: dict):
    prompt = user_input.get("prompt", "")
    ai_response = await fetch_ai_response(prompt)
    return {"response": ai_response}
