import requests
import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def call_ollama(prompt: str) -> str:
    config = load_config()

    payload = {
        "model": config["model"],
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(config["ollama_url"], json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama: {e}")
        return ""