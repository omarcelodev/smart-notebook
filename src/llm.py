import requests
from prompts import SYSTEM_PROMPT


OLLAMA_URL = "http://localhost:11434/api/chat"


def ask_llm(text: str, model: str) -> str:

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": text
            }
        ],
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    data = response.json()
    try:
        return data["message"]["content"]
    except (KeyError, TypeError):
        raise ValueError(f"Formato inesperado da resposta: {data}")

    return data["message"]["content"]