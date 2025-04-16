from app.llm.ollama_client import ask_ollama

async def get_fortune(name: str) -> dict:
    prompt = "오늘 운세를 알려줘."
    result = await ask_ollama(prompt)
    return {
        "name": name,
        "fortune": f"{name}님의 운세는 다음과 같습니다:\n{result.strip()}"
    }