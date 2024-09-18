# conversation/action_handler.py
from intents.intent_base import IntentBase

class ActionHandler:
    def __init__(self, intents):
        self.intents = intents

    def handle_intent(self, message: str) -> str:
        for intent in self.intents:
            if intent.can_handle(message):
                return intent.handle(message)
        return None  # No se encontró un intent que pueda manejar el mensaje
