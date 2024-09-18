# intents/api_intent.py
from intents.intent_base import IntentBase

class ApiIntent(IntentBase):
    def __init__(self, api_service):
        self.api_service = api_service

    def can_handle(self, message: str) -> bool:
        return 'llamar api' in message.lower()

    def handle(self, message: str) -> str:
        response = self.api_service.call_api()
        return f"Respuesta de la API: {response}"
