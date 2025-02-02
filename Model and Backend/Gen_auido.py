from gtts import gTTS
import os

def Gen_auido(caption):
    # Language in which you want to convert
    language = 'en'

    # Creating an instance of gTTS
    speech = gTTS(text=caption, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named "caption.mp3"
    speech.save("caption.mp3")

