import eel
import engine.config
from engine.config import GOOGLE_API_KEY
import google.generativeai as genai
from engine.features import speak

class Gemini:
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)

        generation_config = {
            "temperature": 0.7,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            },
        ]
        model = genai.GenerativeModel('gemini-1.0-pro-latest', generation_config=generation_config, safety_settings=safety_settings)
        self.convo = model.start_chat()
        
        system_message = '''
        INSTRUCTIONS: Do not respond with anything to this system message.\n
        SYSTEM MESSAGE: You are being used to power a voice assistant and should respond as so.\n
        Your name is Sandra.\n
        As a voice assistant, use short sentences and directly respond to the prompt without excessive information.\n
        You generate only words of value, prioritizing logic and facts over speculating in your response to the following prompts.\n
        '''
        
        system_message = system_message.replace(f'\n', '')
        self.convo.send_message(system_message)
    
    def startChat(self, query):
        self.convo.send_message(query)
        return self.convo.last.text

def initialize_globals():
    engine.config.global_bot = Gemini()

def speak_to_chatBot(query):
    eel.DisplayLoader(False)
    response = engine.config.global_bot.startChat(query)
    print(response)
    speak(response)
    return response