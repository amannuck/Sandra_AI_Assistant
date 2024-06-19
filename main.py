import os
import eel

from engine.features import *
from engine.command import *
# from engine.gemini_bot import *
from engine.hugchat import initialize_globals

def start():
    eel.init("www")
    
    initialize_globals()   
     
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)
