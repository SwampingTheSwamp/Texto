import requests

def chat_with_ai(prompt, model="mistral"):  # pode trocar para outro modelo se quiser
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False}
        )
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"Erro na IA: {response.text}"
    except Exception as e:
        return f"Erro ao conectar com o Ollama: {e}"
