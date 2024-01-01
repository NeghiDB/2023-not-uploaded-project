#importations for gtts
from gtts import gTTS
import os

#########################################################################
#convert from text to speech
text = query
language = 'en'
speech = gTTS(text = text, lang = language, slow = True)
speech.save("text.mp3")
#os.system("start text.mp3")
#########################################################################