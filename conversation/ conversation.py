# conversation/conversation.py
import os
import openai
from utils.dependency_injector import build_action_handler

class Conversation:
    def __init__(self):
        self.messages = []
        self.action_handler = build_action_handler()
        openai.api_key = os.getenv("OPENAI_API_KEY")  # Reemplaza con tu clave de API

    def add_message(self, role, content):
        self.messages.append({'role': role, 'content': content})

    def get_response(self):
        user_message = self.messages[-1]['content']

        # Intentar manejar el mensaje con un intent
        action_response = self.action_handler.handle_intent(user_message)
        if action_response:
            assistant_message = action_response
        else:
            # Si ningún intent puede manejar el mensaje, usar OpenAI API
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=self.messages
            )
            assistant_message = response['choices'][0]['message']['content']

        self.add_message('assistant', assistant_message)
        return assistant_message
