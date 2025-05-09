from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Caminho onde o modelo foi salvo após o treino
model_dir = "utils/gpt2_model"

# Carrega modelo e tokenizer
model = GPT2LMHeadModel.from_pretrained(model_dir)
tokenizer = GPT2Tokenizer.from_pretrained(model_dir)

model.eval()

def chat_with_gpt2(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(
        inputs["input_ids"],
        max_new_tokens=100,  # <-- use isso ao invés de max_length
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        no_repeat_ngram_size=2,
        pad_token_id=tokenizer.eos_token_id  # isso evita warnings de pad_token_id
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
