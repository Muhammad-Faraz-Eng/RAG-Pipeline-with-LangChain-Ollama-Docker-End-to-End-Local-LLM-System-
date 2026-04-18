import requests

OLLAMA_URL = "http://ollama:11434/api/generate"


def ask_llm(prompt, model="tinyllama"):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
        },
    )

    return response.json()["response"]
