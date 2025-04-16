import httpx

OLLAMA_URL = "http://localhost:11434/api/generate"

async def ask_ollama(prompt: str, model: str = "gemma:2b"):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            OLLAMA_URL,
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=30
        )
        response.raise_for_status()
        return response.json().get("response")