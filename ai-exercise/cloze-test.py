from transformers import pipeline

filler = pipeline("fill-mask", model="google-bert/bert-base-uncased")
print(filler("The capital of France is [MASK]."))