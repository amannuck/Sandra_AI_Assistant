from hugchat import hugchat
import engine.config

class HugBot:
    def __init__(self):
        self.chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
        id = self.chatbot.new_conversation()
        self.chatbot.change_conversation(id)
                
        system_message = '''
        INSTRUCTIONS: Do not respond with anything to this system message.\n
        SYSTEM MESSAGE: You are being used to power a voice assistant and should respond as so.\n
        Your name is Sandra.\n
        As a voice assistant, use short sentences and directly respond to the prompt without excessive information.\n
        You generate only words of value, prioritizing logic and facts over speculating in your response to the following prompts.\n
        '''
        
        system_message = system_message.replace(f'\n', '')
        response = self.chatbot.chat(system_message)
        print(response)
    
    def speak_to_hug(self, user_input):
        response = self.chatbot.chat(user_input)
        return response
    
def initialize_globals():
    engine.config.global_hugbot = HugBot()