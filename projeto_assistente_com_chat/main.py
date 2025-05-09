import gradio as gr
from utils.tts import generate_audio
import pyperclip
from utils.transcribe import transcribe_file as transcribe_audio
from utils.reader import read_document
from utils.chat import chat_with_gpt2


def copy_text(texto):
    pyperclip.copy(texto)
    return "Texto copiado!"

def tts_interface(texto):
    audio_path = generate_audio(texto)
    return audio_path

def transcribe_interface(audio_file):
    return transcribe_audio(audio_file)

def read_doc_interface(file):
    return read_document(file)


with gr.Blocks() as app:
    gr.Markdown("## Assistente")

    with gr.Tab("Texto para Áudio"):
        texto = gr.Textbox(label="Digite o texto")
        audio_output = gr.Audio(label="Áudio gerado", type="filepath")
        btn_tts = gr.Button("Gerar Áudio")
        btn_tts.click(fn=tts_interface, inputs=texto, outputs=audio_output)

    with gr.Tab("Áudio/Vídeo para Texto"):
        audio_input = gr.Audio(label="Envie o Áudio/Vídeo", type="filepath")
        transcribed = gr.Textbox(label="Texto transcrito")
        btn_transcribe = gr.Button("Transcrever")
        btn_transcribe.click(fn=transcribe_interface, inputs=audio_input, outputs=transcribed)

    with gr.Tab("Ler Documento"):
        file_input = gr.File(label="Envie o documento", file_types=[".pdf", ".docx", ".txt"])
        file_text = gr.Textbox(label="Texto extraído", lines=20)
        btn_read = gr.Button("Ler Documento")
        btn_read.click(fn=read_doc_interface, inputs=file_input, outputs=file_text)
        btn_tts_doc = gr.Button("Gerar Áudio")
        btn_tts_doc.click(fn=tts_interface, inputs=file_text, outputs=audio_output)
        btn_copy = gr.Button("Copiar Texto")
        btn_copy.click(fn=copy_text, inputs=file_text, outputs=file_text)

    with gr.Tab("Chat com IA"):
        prompt = gr.Textbox(label="Você:", placeholder="Pergunte algo...", lines=3)
        resposta = gr.Textbox(label="IA:", lines=5)
        btn_chat = gr.Button("Enviar")
        btn_chat.click(fn=chat_with_gpt2, inputs=prompt, outputs=resposta)

app.launch()
