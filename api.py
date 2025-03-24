from flask import Flask, request, jsonify, send_file
from utils import fetch_news, analyze_sentiment, generate_tts, comparative_sentiment_analysis, extract_key_topics, generate_comparative_analysis
import os

app = Flask(__name__)

@app.route('/get_news', methods=['GET'])
def get_news():
    company_name = request.args.get('company')
    if not company_name:
        return jsonify({"error": "Company name is required"}), 400

    articles = fetch_news(company_name)
    if not articles:
        return jsonify({"error": "No articles found"}), 404

    sentiment_summary = comparative_sentiment_analysis(articles)
    topics = extract_key_topics(articles)
    comparison = generate_comparative_analysis(articles)

    return jsonify({
        "company": company_name,
        "articles": articles,
        "comparative_sentiment": sentiment_summary,
        "key_topics": topics,
        "comparative_coverage": comparison
    })

@app.route('/generate_tts', methods=['POST'])
def generate_audio():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "Text content is required"}), 400

    filename = "output.mp3"
    generate_tts(text, filename)

    if os.path.exists(filename):
        print(f"✅ File successfully created: {filename}")
        return send_file(filename, as_attachment=True)
    else:
        print(f"❌ Error: File '{filename}' not found!")
        return jsonify({"error": "Failed to generate audio"}), 500

if __name__ == '__main__':
    app.run(debug=True)
