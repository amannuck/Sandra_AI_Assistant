import time
import pyttsx3
import speech_recognition as sr
from speech_recognition.recognizers import google
import eel
from engine.config import ASSISTANT_NAME

@eel.expose
def speak(text):
    text = str(text)
    engine = pyttsx3.init()
    
    #Voice change
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    
    #Rate
    engine.setProperty('rate', 170) 
    
    #Volume
    engine.setProperty('volume', 1.0) 
    eel.DisplayLoader(True)
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
        r.energy_threshold = 4000
        r.adjust_for_ambient_noise(source, duration=0.2)
        
        audio = r.listen(source, 10, 6)
    
    try:
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio)
        print(f'user said: {query}')
        eel.DisplayMessage(query)
        time.sleep(2)
        
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
    
    query = query.replace(ASSISTANT_NAME, "")


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
    except Exception as e:
        print(e)
        
    eel.ShowHood()

        
        
         