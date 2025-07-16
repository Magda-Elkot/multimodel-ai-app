from transformers import pipeline

#load the sentiment analysis model 
sentiment_model =  pipeline("sentiment-analysis")

def predict_sentiment(text):
    result = sentiment_model(text)
    return result
