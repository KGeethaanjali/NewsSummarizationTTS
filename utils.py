import os
from gtts import gTTS
from googletrans import Translator

translator = Translator()

def generate_tts(text, filename="output.mp3"):
    """Convert English text to Hindi and generate speech using gTTS."""
    translated_text = translator.translate(text, dest="hi").text
    tts = gTTS(translated_text, lang="hi")
    tts.save(filename)

    # DEBUG: Check if the file was created
    if os.path.exists(filename):
        print(f"✅ TTS file successfully created: {filename}")
    else:
        print(f"❌ ERROR: TTS file '{filename}' was not created!")

    return filename
