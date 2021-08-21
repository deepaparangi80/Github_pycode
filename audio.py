from gtts import gTTS
from playsound import playsound
audio = "speech.mp3"
language = 'en'
sp = gTTS(text = "welcome to my channel,please subscribe to my channel")
sp.save(audio)
playsound(audio)
print("----playing audio-------")