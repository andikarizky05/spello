from transformers import pipeline

# Menggunakan pipeline NLP dari Hugging Face untuk penyederhanaan teks
simplifier = pipeline("text2text-generation", model="t5-small")

def simplify_text(text: str) -> str:
    prompt = "simplify: " + text
    result = simplifier(prompt, max_length=512, do_sample=False)
    return result[0]['generated_text']
