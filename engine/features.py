from playsound import playsound
import eel
import os
from engine.config import ACCESS_KEY
from engine.command import speak
import pywhatkit as kit
from engine.db import cursor
import webbrowser
from engine.helper import extract_yt_term, extract_app_name
import time
import pvporcupine
import struct
import pyaudio
from hugchat import hugchat

@eel.expose
def playAssistantSound():
    music_dir= "www\\assets\\sounds\\audio1.mp3"
    playsound(music_dir)

def openCommand(query):
    app_name = extract_app_name(query)
    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+app_name)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+app_name)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+app_name)
                    try:
                        os.system('start '+ app_name)
                    except:
                        speak("not found")
        except:
            speak("I think something went wrong. Please try again.")
    else:
        speak("Sorry, I didn't quit get that. Please try again.")
        
def playYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on Youtube")
    kit.playonyt(search_term)

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        keyword_paths = ['www\\assets\\keywords\\sandra.ppn',]
        porcupine=pvporcupine.create(access_key=ACCESS_KEY, keyword_paths=keyword_paths) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("wake word detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response
