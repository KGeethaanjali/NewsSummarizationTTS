import requests
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from gtts import gTTS
from googletrans import Translator
from collections import Counter
import re

nltk.download('vader_lexicon')
nltk.download('stopwords')

sia = SentimentIntensityAnalyzer()
translator = Translator()

def fetch_news(company_name):
    """Fetch news articles from NewsAPI.org."""
    api_key = "d31f208854bc446ab23b26da7bf6ee6f"
    url = f"https://newsapi.org/v2/everything?q={company_name}&language=en&pageSize=10&apiKey={api_key}"
    
    response = requests.get(url)
    if response.status_code != 200:
        return []

    data = response.json()
    articles = []

    for item in data.get("articles", []):
        title = item["title"]
        link = item["url"]
        summary = item["description"] or item["content"] or "No summary available"
        
        articles.append({
            "title": title,
            "link": link,
            "summary": summary,
            "sentiment": analyze_sentiment(summary)
        })

    return articles

def analyze_sentiment(text):
    """Analyze sentiment of the given text using VADER."""
    score = sia.polarity_scores(text)
    if score["compound"] >= 0.05:
        return "Positive"
    elif score["compound"] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def comparative_sentiment_analysis(articles):
    """Summarize sentiment distribution across all articles."""
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for article in articles:
        sentiment_counts[article["sentiment"]] += 1

    return {
        "Sentiment Distribution": sentiment_counts,
        "Overall Sentiment": max(sentiment_counts, key=sentiment_counts.get)
    }

def generate_tts(text, filename="output.mp3"):
    """Convert English text to Hindi and then generate speech using gTTS."""
    translated_text = translator.translate(text, dest="hi").text
    tts = gTTS(translated_text, lang="hi")
    tts.save(filename)
    return filename

def extract_key_topics(articles, top_n=5):
    """Extract top key topics from the article summaries."""
    all_text = " ".join(article["summary"] for article in articles)
    words = re.findall(r'\b\w+\b', all_text.lower())
    stopwords = set(nltk.corpus.stopwords.words('english'))
    keywords = [word for word in words if word not in stopwords and len(word) > 3]
    most_common = Counter(keywords).most_common(top_n)
    return [topic for topic, _ in most_common]

def generate_comparative_analysis(articles):
    """Generate a comparative view of sentiment by title/source."""
    comparison_data = []

    for article in articles:
        comparison_data.append({
            "title": article["title"],
            "link": article["link"],
            "sentiment": article["sentiment"]
        })

    return comparison_data
