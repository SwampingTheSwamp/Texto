import edge_tts
import asyncio
import uuid
import os

async def _run():
    texto = "Texto de exemplo"
    output_path = f"temp/{uuid.uuid4().hex}.mp3"

    # Garante que a pasta 'temp/' exista
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    communicate = edge_tts.Communicate(texto, "pt-BR-FranciscaNeural")
    await communicate.save(output_path)

def generate_audio(texto):
    output_path = f"temp/{uuid.uuid4().hex}.mp3"

    async def _run():
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        communicate = edge_tts.Communicate(texto, "pt-BR-FranciscaNeural")
        await communicate.save(output_path)

    asyncio.run(_run())
    return output_path
