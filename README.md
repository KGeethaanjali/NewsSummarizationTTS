# NewsSummarizationTTS
📰 News Summarization & Sentiment Analysis with Hindi TTS
This project is a web-based application that allows users to:

Fetch the latest news articles about a company.

Analyze the sentiment of each article using NLP.

Perform a comparative sentiment analysis.

Convert the summary report into Hindi audio using Text-to-Speech (TTS).

Built with Flask, Streamlit, NLTK, Google Translate, and gTTS.

 Features
 News Fetching – Get top 10 news articles about a company via NewsAPI.

 Sentiment Analysis – Classify article summaries as Positive, Negative, or Neutral.

 Topic Extraction – Identify the most common keywords in each article.

 Comparative Report – Analyze topic and sentiment differences across articles.

 Hindi TTS – Generate Hindi speech from the sentiment summary.

 Tech Stack
Backend: Flask (REST API)

Frontend: Streamlit (interactive UI)

NLP: NLTK's VADER for sentiment, tokenization, stopwords

TTS: Google Translate + gTTS for Hindi audio output

API: NewsAPI.org

🛠 Installation
Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/NewsSummarizationTTS.git
cd NewsSummarizationTTS
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Download NLTK resources These will be downloaded automatically when you run the app.

▶ Running the App
1. Start the Flask API
bash
Copy
Edit
python api.py
2. Start the Streamlit frontend (in a new terminal)
bash
Copy
Edit
streamlit run app.py
Make sure both are running concurrently.

 Usage
Enter a company name (e.g., "Tesla").

Click "Fetch News & Analyze Sentiment".

Review article summaries, topics, and sentiment.

Click "Generate Hindi Speech" to download and play the summary in Hindi.

 Sample Output
Article Title: Tesla delivers record number of EVs in Q1

Summary: Tesla reported a record-breaking delivery of EVs in the first quarter...

Sentiment: Positive

Topics: ['tesla', 'record', 'evs', 'quarter', 'delivery']

 Folder Structure
bash
Copy
Edit
├── api.py                # Flask backend
├── app.py                # Streamlit UI
├── utils.py              # TTS utilities
├── requirements.txt      # Project dependencies
└── README.md             # You're here!
📄 License
MIT License © 2025 Gitanjali Kavety