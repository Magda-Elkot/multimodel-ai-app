multimodel-ai-app/
│
├── app.py                             # Main Flask application
├── requirements.txt                   # Python dependencies (optional)
│
├── 📁 model/                          # Model logic
│   ├── __init__.py                    # Exports functions from models
│   ├── bert_model.py                  # BERT sentiment analysis logic
│   ├── distilbert_model.py            # DistilBERT sentiment logic
│   ├── roberta_model.py              # RoBERTa sentiment logic
│   └── sentiment.py                   # Aggregates model import/export
│
├── 📁 templates/                      # HTML templates for rendering pages
│   ├── home.html                      # Main homepage
│   ├── nlp.html                       # NLP domain landing page
│   ├── sentiment_form.html           # Form to choose model + enter input
│   ├── sentiment_result.html         # General sentiment result page
│   ├── sentiment_bert.html           # Detailed result & architecture for BERT
│   ├── sentiment_roberta.html        # (To be added) Detailed for RoBERTa
│   ├── sentiment_distilbert.html     # (To be added) Detailed for DistilBERT
│
├── 📁 static/                         # Static assets (CSS, images)
│   ├── style.css                      # Cute and large font styling
│   └── bert_diagram.png              # Visual for BERT architecture
│
└── 📁 __pycache__/                    # Auto-generated Python cache (can ignore)
