import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
print(voices[1].id)
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("hello mota ben, Good evening")
    speak("All the best for your examination")
    speak("as an AI , i predict that you are going to top tommorows examination")
