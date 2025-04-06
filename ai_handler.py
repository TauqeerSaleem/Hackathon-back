import ollama
import asyncio

class AIHandler():
    def __init__(self, model="llama3.2:1b"):
        self.model = model

    async def get_response(self, prompt: str, history=None, name=None, level=None, major=None, year=None, career_goal=None):
        client = ollama.AsyncClient()

        system_prompt = (
            f"You are Ismail, an academic advisor AI helping students at Luddy School of Informatics.\n"
            f"Student name: {name or 'Unknown'}\n"
            f"Level: {level or 'Unknown'}\n"
            f"Major: {major or 'Unknown'}\n"
            f"Year: {year or 'Unknown'}\n"
            f"Career Goal: {career_goal or 'Unknown'}\n\n"
            "Only answer questions related to academic planning, courses, prerequisites, scheduling, credit hours, and degree goals. "
            "If the user asks anything unrelated, politely respond: "
            "'I'm only able to assist with course selection and academic planning questions.'"
        )

        messages = [{"role": "system", "content": system_prompt}]

        # Append previous chat history if provided
        if history:
            messages.extend(history)

        # Add current prompt
        messages.append({"role": "user", "content": prompt})

        response = await client.chat(model=self.model, messages=messages)
        return response["message"]["content"]

# ✅ Updated to accept additional context
async def fetch_ai_response(prompt, history=None, name=None, level=None, major=None, year=None, career_goal=None):
    ai = AIHandler()
    response = await ai.get_response(
        prompt=prompt,
        history=history,
        name=name,
        level=level,
        major=major,
        year=year,
        career_goal=career_goal
    )
    return response
