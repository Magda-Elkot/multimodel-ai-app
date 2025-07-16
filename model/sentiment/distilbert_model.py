from transformers import pipeline
# Load the DistilBERT model for sentiment analysis
distilbert_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
def predict_sentiment(text):
    return distilbert_model(text)