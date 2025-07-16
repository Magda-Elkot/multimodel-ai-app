from transformers import pipeline

# Load the BERT model for sentiment analysis
bert_model = pipeline("sentiment-analysis", model="bert-base-uncased")

def analyze_sentiment(text):
    return bert_model(text)
