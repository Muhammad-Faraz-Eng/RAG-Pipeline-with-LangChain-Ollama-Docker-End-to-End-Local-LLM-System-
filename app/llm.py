import requests
import json

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

    llm_response = response.json()["response"]
    print(f"\n--- RAW LLM RESPONSE ---\n{llm_response}\n")
    
    try:
        json_response = json.loads(llm_response)
        print(f"--- PARSED JSON ---\n{json_response}\n")
        return json_response["answer"]
    except (json.JSONDecodeError, KeyError) as e:
        print(f"--- JSON PARSE ERROR: {e} ---\n")
        return llm_response.strip()
