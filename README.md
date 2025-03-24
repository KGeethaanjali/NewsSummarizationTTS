# NewsSummarizationTTS
# 📰 News Summarization & Hindi TTS

A web app that fetches the latest news articles about a company, performs sentiment analysis, and converts the summary into **Hindi audio** using Text-to-Speech.
---

##  Features

-  **Fetch News** — Get top 10 news articles using [NewsAPI](https://newsapi.org)
-  **Sentiment Analysis** — Classify each article as Positive, Negative, or Neutral using NLTK VADER
-  **Summarization** — Combine summaries and generate overall sentiment trends
-  **Translation** — Translate the entire report to **Hindi** using LibreTranslate API
-  **Text-to-Speech (TTS)** — Generate and play Hindi audio using `gTTS`

---

## 🚀 Live Demo

👉 [Try it on Hugging Face Spaces](https://huggingface.co/spaces/your-username/your-space-name)

> Replace the above URL with your actual Hugging Face Space link.

---

## 🛠 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Pure Python (no Flask required)
- **NLP:** NLTK (VADER sentiment analysis)
- **Translation:** LibreTranslate API (free, no authentication required)
- **Text-to-Speech:** Google Text-to-Speech (`gTTS`)
- **News API:** [NewsAPI.org](https://newsapi.org)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/NewsSummarizationTTS.git
cd NewsSummarizationTTS
pip install -r requirements.txt

streamlit run app.py
.
├── app.py               # Main Streamlit application
├── requirements.txt     # List of required Python packages
└── README.md            # Project documentation

📄 License
This project is licensed under the MIT License.

Author
K Geethaanjali
