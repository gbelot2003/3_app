# intents/chroma_query_intent.py
from intents.intent_base import IntentBase

class ChromaQueryIntent(IntentBase):
    def __init__(self, chroma_service):
        self.chroma_service = chroma_service

    def can_handle(self, message: str) -> bool:
        trigger_phrases = ['consultar datos', 'buscar en archivos']
        return any(phrase in message.lower() for phrase in trigger_phrases)

    def handle(self, message: str) -> str:
        query_text = self.extract_query(message)
        if query_text:
            result = self.chroma_service.query(query_text)
            return f"Resultado de la consulta: {result}"
        else:
            return "Por favor, proporciona una consulta para buscar en los datos."

    def extract_query(self, message: str) -> str:
        trigger_phrases = ['consultar datos', 'buscar en archivos']
        for phrase in trigger_phrases:
            if phrase in message.lower():
                return message.lower().split(phrase)[-1].strip()
        return ''
