from flask import Flask, render_template, request
from model.sentiment import analyze_bert, predict_distilbert, classify_roberta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sentiment', methods=['POST'])
def analyze_sentiment():
    text = request.form['text']
    model_choice = request.form['model_choice']
    
    if model_choice == 'distilbert':
        sentiment = predict_distilbert(text)
    elif model_choice == 'bert':
        sentiment = analyze_bert(text)
    elif model_choice == 'roberta':
        sentiment = classify_roberta(text)
    else:
        sentiment = "Invalid model choice"
        
    return render_template('sentiment.html', sentiment=sentiment, text=text)

if __name__ == '__main__':
    app.run(debug=True)
