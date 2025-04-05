import ollama
import asyncio

class AIHandler():
    def __init__(self, model="llama3.2:1b"):
        self.model = model

    async def get_response(self, prompt: str):
        client = ollama.AsyncClient()

        messages = [{"role": "user", "content": prompt}]

        response = await client.chat(model=self.model, messages=messages)

        return response["message"]["content"]

# Example function to call asynchronously from routes
async def fetch_ai_response(prompt):
    ai = AIHandler()
    response = await ai.get_response(prompt)
    return response