from flask import Flask, render_template, request
from model.sentiment import analyze_bert, predict_distilbert, classify_roberta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


# ---------- NLP Main Page ----------
@app.route('/nlp')
def nlp():
    return render_template('nlp.html')  # Page with NLP tasks (e.g., Sentiment)


# ---------- Sentiment Form ----------
@app.route('/nlp/sentiment')
def sentiment_form():
    return render_template('sentiment_form.html')  # Choose model + input text


# ---------- Sentiment Result ----------
@app.route('/nlp/sentiment/result', methods=['POST'])
def sentiment_result():
    text = request.form['text']
    model_choice = request.form['model_choice']

    # Handle each model choice separately
    if model_choice == 'bert':
        sentiment = analyze_bert(text)
        return render_template('sentiment_bert.html', sentiment=sentiment, text=text)

    elif model_choice == 'distilbert':
        sentiment = predict_distilbert(text)
        return render_template('sentiment_distilbert.html', sentiment=sentiment, text=text)

    elif model_choice == 'roberta':
        sentiment = classify_roberta(text)
        return render_template('sentiment_roberta.html', sentiment=sentiment, text=text)

    else:
        return render_template('error.html', message="Invalid model selection.")

# ---------- Run the App ----------
if __name__ == '__main__':
    app.run(debug=True)
