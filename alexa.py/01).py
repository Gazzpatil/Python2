import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
print(voices[1].id)
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")

    elif hour >= 12 and hour<17:
        speak("Good afternoon")
    else:
        speak("Good evening,ash")    
    speak("I am your assistance sirr,Please tell me how may i help you")    

def takeCommand():
    #It takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing!!")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said:{query}\n")

    except Exception as e:
        #print()
        print("say that once again please.....")
        return "None"
    return query




        
if __name__ == "__main__":
    wishMe()
    #while True:
    if 1: 
        query = takeCommand().lower()   

        #logic for executing tasks based on query

        if "wikipedia" in query:
            speak("Searching Wikipedia....")
            query = query.replace ("wikipedia","")
            results =wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")

        elif "play music" in query:
            music_dir ="D:\\Non Critical\\songs\\Favorite Songs2"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")

        elif "open sundar" in query:
            path="C:\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        
 