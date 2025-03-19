if st.button("🗣 Generate Hindi Speech"):
    if company_name:
        response = requests.get(f"http://127.0.0.1:5000/get_news?company={company_name}")

        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])

            if articles:
                headlines = " | ".join([article["title"] for article in articles])  # Concatenate headlines
                response = requests.post("http://127.0.0.1:5000/generate_tts", json={"text": headlines})

                if response.status_code == 200:
                    audio_file = "output.mp3"
                    st.audio(audio_file)
                else:
                    st.write("❌ Error generating speech.")
            else:
                st.write("⚠ No articles found.")
        else:
            st.write("❌ Error fetching data. Try again.")
