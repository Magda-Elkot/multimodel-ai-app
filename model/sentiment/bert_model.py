from transformers import pipeline

# Load the BERT model
bert_model = pipeline("sentiment-analysis", model="bert-base-uncased")

def analyze_sentiment(text):
    result = bert_model(text)[0]
    label = result['label']
    
    # Map label to Positive/Negative
    sentiment = "Positive" if label == "LABEL_1" else "Negative"

    return {
        "label": sentiment,
        "score": round(result['score'], 3)  # Optional: round for clean UI
    }

