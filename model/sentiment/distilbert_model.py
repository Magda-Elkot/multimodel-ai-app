from transformers import pipeline

distilbert_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def predict_sentiment(text):
    result = distilbert_model(text)[0]
    label = result['label']
    sentiment = "Positive" if label == "POSITIVE" else "Negative"
    
    return {
        "label": sentiment,
        "score": round(result['score'], 3)
    }
