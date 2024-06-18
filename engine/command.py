import pyttsx3
import speech_recognition as sr
from speech_recognition.recognizers import google
import eel
import time

@eel.expose
def speak(text):
    text = str(text)
    engine = pyttsx3.init()
    
    #Voice change
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    
    #Rate
    engine.setProperty('rate', 160) 
    
    #Volume
    engine.setProperty('volume', 1.0) 
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        eel.DisplayMessage('Listening...')
        # r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.2)
        
        audio = r.listen(source, 10, 6)
    
    try:
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio)
        print(f'user said: {query}')
        eel.DisplayMessage(query)
        speak(query)
    except Exception as e:
        return "Oops, I didn't quite get that."
    
    return query.lower()

@eel.expose
def allCommands(message=1):
    
    if message == 1:
        query = takecommand()
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import playYoutube
            playYoutube(query)

        else:
            from engine.features import chatBot
            chatBot(query)
    except:
        print("Error")
        
    eel.ShowHood()

        
        
         