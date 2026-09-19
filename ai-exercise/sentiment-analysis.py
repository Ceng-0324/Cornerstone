import os
import logging

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
logging.basicConfig(level=logging.DEBUG)

print("script start")

from transformers import pipeline

classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion")

print("model loaded, ready to classify text.")

for text in ["I love programming!", "I hate bugs.", "I'm feeling neutral about this."]:
    result = classifier(text)
    print(f"Text: {text} => Emotion: {result[0]['label']}, Score: {result[0]['score']:.4f}")