import os
import streamlit as st
import requests

st.title("📢 News Summarization & Hindi TTS")

company_name = st.text_input("🔍 Enter Company Name:", "")

if st.button("🔎 Fetch News & Analyze Sentiment"):
    if company_name:
        response = requests.get(f"http://127.0.0.1:5000/get_news?company={company_name}")

        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])

            if articles:
                for article in articles:
                    st.subheader(article["title"])
                    st.write(article["summary"])
                    st.write(f"**Sentiment:** {article['sentiment']}")
                    st.write(f"[Read more]({article['link']})")

                # Store the report for TTS conversion
                st.session_state["full_report"] = " ".join([article["title"] + ": " + article["summary"] for article in articles])
            else:
                st.write("⚠ No articles found.")
        else:
            st.write("❌ Error fetching data. Try again.")

if st.button("🗣 Generate Hindi Speech"):
    if "full_report" in st.session_state:
        response = requests.post("http://127.0.0.1:5000/generate_tts", json={"text": st.session_state["full_report"]})

        if response.status_code == 200:
            # Save the file
            with open("output.mp3", "wb") as f:
                f.write(response.content)

            if os.path.exists("output.mp3"):
                st.audio("output.mp3", format="audio/mp3")
            else:
                st.write("⚠ ERROR: File not found after generation.")
        else:
            st.write("❌ Error generating speech.")
    else:
        st.write("⚠ No news report available for TTS.")
