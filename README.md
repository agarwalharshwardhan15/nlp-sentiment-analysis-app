NLP Sentiment Analysis App

A simple web application built with Streamlit and TextBlob that analyzes the sentiment of user-entered text and classifies it as Positive, Negative, or Neutral, along with a polarity score.

Features
Clean, interactive web UI (no web development knowledge required)
Real-time sentiment classification using NLP
Displays a polarity score ranging from -1.0 (very negative) to +1.0 (very positive)
Lightweight and runs entirely on your local machine
Tech Stack
Python 3
Streamlit — for the web interface
TextBlob — for NLP-based sentiment analysis
How It Works
The user enters any text into the input box.
On clicking Analyze, the text is passed to TextBlob, which computes a polarity score based on the words and phrases used.
The app classifies the result as:
Positive if polarity > 0
Negative if polarity < 0
Neutral if polarity = 0
Project Structure
nlp-sentiment-app/
├── app.py                 # Streamlit UI
├── sentiment_model.py     # Core NLP sentiment analysis logic
├── requirements.txt       # Python dependencies
└── .gitignore
Setup & Installation
Clone the repository
bash
   git clone https://github.com/agarwalharshwardhan15/nlp-sentiment-analysis-app.git
   cd nlp-sentiment-analysis-app
Create and activate a virtual environment
bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
Install dependencies
bash
   pip install -r requirements.txt
Run the app
bash
   streamlit run app.py
Open the local URL shown in the terminal (typically http://localhost:8501) in your browser.
Example

Input: I really enjoyed this. Output: Sentiment: Positive | Polarity Score: 0.50

Future Improvements
Train a custom ML classifier (Logistic Regression / Naive Bayes) on a labeled dataset for improved accuracy
Upgrade to a transformer-based model (e.g., BERT) for more nuanced sentiment detection
Add support for batch analysis via CSV upload
Deploy the app publicly using Streamlit Community Cloud
Author

Harshwardhan Agarwal