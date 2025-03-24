import streamlit as st
import requests
import os

st.title("📢 News Summarization & Hindi TTS")

company_name = st.text_input("🔍 Enter Company Name:", "")

if st.button("📰 Fetch Headlines"):
    if company_name:
        response = requests.get(f"http://127.0.0.1:5000/get_news?company={company_name}")

        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])
            sentiment_summary = data.get("comparative_sentiment", {})

            if articles:
                st.subheader("🧾 Top Headlines")
                for article in articles:
                    st.markdown(f"**📰 {article['title']}**")
                    st.markdown(f"- Sentiment: `{article['sentiment']}`")
                    st.markdown(f"[🔗 Read more]({article['link']})")
                    st.markdown("---")
                
                st.session_state["headlines"] = " | ".join([article["title"] for article in articles])

                st.markdown("### 📊 Overall Sentiment Summary")
                st.json(sentiment_summary)

                st.markdown("### 🔑 Key Topics Extracted")
                st.write(", ".join(data.get("key_topics", [])))

                st.markdown("### 📋 Comparative Coverage Summary")
                for item in data.get("comparative_coverage", []):
                    st.markdown(f"**📰 {item['title']}**")
                    st.markdown(f"- Sentiment: `{item['sentiment']}`")
                    st.markdown(f"[🔗 Read more]({item['link']})")
                    st.markdown("---")

            else:
                st.warning("No articles found.")
        else:
            st.error("Failed to fetch news. Check API or internet connection.")

if "headlines" in st.session_state:
    if st.button("🗣 Generate Hindi Speech"):
        tts_response = requests.post("http://127.0.0.1:5000/generate_tts", json={"text": st.session_state["headlines"]})

        if tts_response.status_code == 200:
            with open("output.mp3", "wb") as f:
                f.write(tts_response.content)

            if os.path.exists("output.mp3"):
                st.audio("output.mp3", format="audio/mp3")
            else:
                st.warning("⚠ File generation failed.")
        else:
            st.error("❌ Error generating speech.")
