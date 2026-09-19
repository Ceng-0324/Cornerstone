import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def my_simple_text_classification(text, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
    # 1.加载分词器、模型
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # 2.分词
    inputs = tokenizer(text, return_tensors="pt", truncation=True)

    # 3.前向传播推理
    with torch.no_grad():
        outputs = model(**inputs)

    # 4.argmax拿到预测类别id
    pred_id = torch.argmax(outputs.logits, dim=-1).item()

    # 5.id映射label名称
    label_name = model.config.id2label[pred_id]
    score = torch.softmax(outputs.logits, dim=-1)[0][pred_id].item()

    # 输出结构对齐官方pipeline
    return [{"label": label_name, "score": score}]

# 测试
out = my_simple_text_classification("I love this movie!")
print("手写pipeline输出: ", out)

# 官方pipeline对比
from transformers import pipeline
official_pipe = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
print("官方pipeline输出: ", official_pipe("I love this movie!"))
