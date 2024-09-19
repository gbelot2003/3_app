# conversation/conversation.py
import os
import openai
from utils.dependency_injector import *
openai.api_key = os.getenv("OPENAI_API_KEY")

class Chat:
    def __init__(self):
        self.messages = []
        self.action_handler = build_action_handler()

    def add_message(self, role, content):
        self.messages.append({'role': role, 'content': content})

    def get_response(self):
        user_message = self.messages[-1]['content']
        action_response = self.action_handler.handle_intent(user_message)
        if action_response:
            assistant_message = action_response
        else:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=self.messages
            )
            assistant_message = response.choices[0].message.content
        self.add_message('assistant', assistant_message)
        return assistant_message
