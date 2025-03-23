from flask import Flask, request, jsonify, send_file
import os
from gtts import gTTS
from googletrans import Translator
import requests
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize Flask App
app = Flask(__name__)

# Initialize Sentiment Analyzer & Translator
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
translator = Translator()

# NewsAPI Key
NEWS_API_KEY = "d31f208854bc446ab23b26da7bf6ee6f"

### 🔹 FUNCTION: Fetch News from NewsAPI
def fetch_news(company_name):
    """Fetch news articles related to the company using NewsAPI."""
    url = f"https://newsapi.org/v2/everything?q={company_name}&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()
    articles = []

    for article in data["articles"][:10]:  # Get top 10 articles
        title = article["title"]
        link = article["url"]
        summary = article["description"] if article["description"] else "No summary available"
        
        articles.append({
            "title": title,
            "link": link,
            "summary": summary,
            "sentiment": analyze_sentiment(summary)
        })

    return articles


### 🔹 FUNCTION: Analyze Sentiment
def analyze_sentiment(text):
    """Analyze sentiment of the given text using VADER."""
    score = sia.polarity_scores(text)
    if score["compound"] >= 0.05:
        return "Positive"
    elif score["compound"] <= -0.05:
        return "Negative"
    else:
        return "Neutral"


### 🔹 FUNCTION: Generate Comparative Sentiment Analysis
def comparative_sentiment_analysis(articles):
    """Summarize sentiment distribution across all articles."""
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for article in articles:
        sentiment_counts[article["sentiment"]] += 1

    return {
        "Sentiment Distribution": sentiment_counts,
        "Overall Sentiment": max(sentiment_counts, key=sentiment_counts.get)
    }


### 🔹 FUNCTION: Generate Hindi Text-to-Speech
def generate_tts(text, filename="output.mp3"):
    """Convert English text to Hindi and generate speech using gTTS."""
    translated_text = translator.translate(text, dest="hi").text
    tts = gTTS(translated_text, lang="hi")
    tts.save(filename)

    if os.path.exists(filename):
        print(f"✅ TTS file successfully created: {filename}")
    else:
        print(f"❌ ERROR: TTS file '{filename}' was not created!")


### 🔹 API Endpoint: Fetch News & Analyze Sentiment
@app.route('/get_news', methods=['GET'])
def get_news():
    """Fetch news and analyze sentiment based on user-inputted company name."""
    company_name = request.args.get('company')
    if not company_name:
        return jsonify({"error": "Company name is required"}), 400

    articles = fetch_news(company_name)
    if not articles:
        return jsonify({"error": "No articles found"}), 404

    sentiment_summary = comparative_sentiment_analysis(articles)

    return jsonify({
        "company": company_name,
        "articles": articles,
        "comparative_sentiment": sentiment_summary
    })


### 🔹 API Endpoint: Generate Hindi Speech (TTS)
@app.route('/generate_tts', methods=['POST'])
def generate_audio():
    """Generate Hindi TTS from the full news report."""
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "Text content is required"}), 400

    filename = "output.mp3"
    generate_tts(text, filename)

    if os.path.exists(filename):
        return send_file(filename, as_attachment=True)
    else:
        return jsonify({"error": "Failed to generate audio"}), 500


### 🔹 Run the Flask App
if __name__ == '__main__':
    app.run(debug=True, port=5000)
