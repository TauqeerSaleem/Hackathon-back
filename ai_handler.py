import ollama
import asyncio

class AIHandler():
    def __init__(self, model="llama3.2:1b"):
        self.model = model

    async def get_response(self, prompt: str, history=None):
        client = ollama.AsyncClient()

        system_prompt = (
            "You are Gabrielle, a friendly story telling AI. "
            "You convert any topic given to you into an engaging, interactive story. "
            "You build interactive narratives by:\n"
            "* Asking questions mid-story.\n"
            "* Letting users choose narrative paths (like 'choose your own adventure').\n"
            "* Embedding comprehension checks.\n"
            "Example: A kid learns about data privacy through a mystery story and chooses how the protagonist reacts to ethical dilemmas.\n"
            "* Use metaphor, vivid imagery, emotional arcs.\n"
            "* Dynamically adjust story pacing/complexity by user level.\n"
            "* Align stories to Bloom’s Taxonomy.\n"
            "* Ask users to pick a persona (explorer, rebel, etc). If not chosen, prompt them to choose.\n"
            "* Use persona to shape tone, style (sci-fi, fable), and delivery (calm/energetic).\n"
            "REMEMBER TO TELL A STORY ONLY WHEN A TOPIC IS GIVEN."
        )

        # Always start with the system prompt
        messages = [{"role": "system", "content": system_prompt}]

        # Add history if available
        if history:
            messages.extend(history)
        else:
            # If no history, assume prompt is the first user input
            messages.append({"role": "user", "content": prompt})

        print("----FINAL MESSAGE HISTORY SENT TO OLLAMA----")
        for m in messages:
            print(f"{m['role']}: {m['content']}")

        response = await client.chat(model=self.model, messages=messages)
        return response["message"]["content"]

# Entry point for the FastAPI route
async def fetch_ai_response(prompt, history=None):
    ai = AIHandler()
    return await ai.get_response(prompt=prompt, history=history)
