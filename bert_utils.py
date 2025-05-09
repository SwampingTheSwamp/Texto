from transformers import pipeline

# Carregando modelos
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
ner_pipeline = pipeline("ner", grouped_entities=True)

def bert_sentiment(texto):
    resultado = sentiment_pipeline(texto)
    return f"{resultado[0]['label']} (confiança: {resultado[0]['score']:.2f})"

def bert_qa(pergunta, contexto):
    resultado = qa_pipeline(question=pergunta, context=contexto)
    return f"{resultado['answer']} (confiança: {resultado['score']:.2f})"

def bert_ner(texto):
    entidades = ner_pipeline(texto)
    resultado = []
    for ent in entidades:
        resultado.append(f"{ent['word']} ({ent['entity_group']}, {ent['score']:.2f})")
    return "\n".join(resultado)
