from transformers import pipeline
# Load the RoBERTa model for sentiment analysis
roberta_model = pipeline("sentiment-analysis", model="roberta-base")
def classify_sentiment(text):
    return roberta_model(text)