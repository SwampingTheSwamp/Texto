from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

model_path = "utils/gpt2_model"  # Ajuste conforme necessário

# Carrega modelo e tokenizer
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

# Garante que o modelo está em avaliação
model.eval()

def chat_with_gpt2(prompt, max_length=150):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_length=max_length,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response[len(prompt):].strip()
