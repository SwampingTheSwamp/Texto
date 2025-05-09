import gradio as gr
from utils.tts import generate_audio
import pyperclip  # Importação do pyperclip
from utils.transcribe import transcribe_file as transcribe_audio
from utils.reader import read_document
from utils.ai_chat import chat_with_ai
from bert_utils import bert_sentiment, bert_qa, bert_ner  # novo


# Função para copiar o conteúdo da caixa de texto
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
    gr.Markdown("## Assitente")
    
    with gr.Tab("Texto para Áudio"):
        texto = gr.Textbox(label="Digite o texto")
        audio_output = gr.Audio(label="Áudio gerado", type="filepath")
        btn_tts = gr.Button("Gerar Áudio")
        btn_tts.click(fn=tts_interface, inputs=texto, outputs=audio_output)

    with gr.Tab("Áudio/Vídeo para Texto"):
        audio_input = gr.File(label="Envie o Áudio/Vídeo", file_types=[".mp3", ".ogg", ".wav", ".mp4", ".mkv", ".avi"])
        transcribed = gr.Textbox(label="Texto transcrito")
        
        btn_transcribe = gr.Button("Transcrever")
        btn_transcribe.click(fn=transcribe_interface, inputs=audio_input, outputs=transcribed)
        btn_copy = gr.Button("Copiar Texto")
        btn_copy.click(fn=copy_text, inputs=transcribed, outputs=transcribed)
        

    with gr.Tab("Ler Documento"):
        file_input = gr.File(label="Envie o documento", file_types=[".pdf", ".docx", ".txt"])
        file_text = gr.Textbox(label="Texto extraído", lines=20)
        audio_output2 = gr.Audio(label="Áudio do Documento", type="filepath")  # Novo componente de áudio
        btn_read = gr.Button("Ler Documento")
        btn_read.click(fn=read_doc_interface, inputs=file_input, outputs=file_text)

        btn_tts_from_file = gr.Button("Gerar Áudio")
        btn_tts_from_file.click(fn=tts_interface, inputs=file_text, outputs=audio_output2)

        btn_copy = gr.Button("Copiar Texto")
        btn_copy.click(fn=copy_text, inputs=file_text, outputs=file_text)

    with gr.Tab("Análise de Sentimento"):
        texto_sentimento = gr.Textbox(label="Digite uma frase")
        sentimento_resultado = gr.Textbox(label="Resultado")
        btn_sentimento = gr.Button("Analisar Sentimento")
        btn_sentimento.click(fn=bert_sentiment, inputs=texto_sentimento, outputs=sentimento_resultado)

    with gr.Tab("Pergunta e Resposta"):
        contexto_qa = gr.Textbox(label="Contexto", lines=10)
        pergunta_qa = gr.Textbox(label="Pergunta")
        resposta_qa = gr.Textbox(label="Resposta")
        btn_qa = gr.Button("Responder")
        btn_qa.click(fn=bert_qa, inputs=[pergunta_qa, contexto_qa], outputs=resposta_qa)
    
    with gr.Tab("Entidades Nomeadas (NER)"):
        texto_ner = gr.Textbox(label="Digite o texto", lines=5)
        resultado_ner = gr.Textbox(label="Entidades encontradas", lines=10)
        btn_ner = gr.Button("Extrair Entidades")
        btn_ner.click(fn=bert_ner, inputs=texto_ner, outputs=resultado_ner)



    


app.launch()
