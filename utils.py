import requests
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from gtts import gTTS
from googletrans import Translator

nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()
translator = Translator()

def analyze_sentiment(text):
    """Analyze sentiment of the given text using VADER."""
    score = sia.polarity_scores(text)
    if score["compound"] >= 0.05:
        return "Positive"
    elif score["compound"] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def generate_tts(text, filename="output.mp3"):
    """Convert English text to Hindi and then generate speech using gTTS."""
    translated_text = translator.translate(text, dest="hi").text  # Translate to Hindi
    tts = gTTS(translated_text, lang="hi")
    tts.save(filename)
    return filename
