from transformers import pipeline

roberta_model = pipeline("sentiment-analysis", model="roberta-base")

def classify_sentiment(text):
    result = roberta_model(text)[0]
    label = result['label']
    
    # Roberta returns "LABEL_0"/"LABEL_1"
    sentiment = "Positive" if label == "LABEL_1" else "Negative"
    
    return {
        "label": sentiment,
        "score": round(result['score'], 3)
    }
