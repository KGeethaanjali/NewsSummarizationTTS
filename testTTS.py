from gtts import gTTS

text = "यह एक परीक्षण है"
tts = gTTS(text, lang='hi')
tts.save("test_output.mp3")
