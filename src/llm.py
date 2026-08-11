import requests
from config import Config
from prompts import SYSTEM_PROMPT


def ask_llm(text: str, config: Config) -> str:

    payload = {
        "model": config.model,
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
        config.ollama_url,
        json=payload,
        timeout=config.timeout
    )

    response.raise_for_status()

    data = response.json()
    try:
        return data["message"]["content"]
    except (KeyError, TypeError):
        raise ValueError(f"Formato inesperado da resposta: {data}")