from transformers import pipeline

generator = pipeline("text-generation", model="openai-community/gpt-2")
print(generator("I enjoy walking with my cute dog", max_new_tokens=20, do_sample=False))