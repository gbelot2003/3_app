# intents/intent_base.py
from abc import ABC, abstractmethod

class IntentBase(ABC):
    @abstractmethod
    def can_handle(self, message: str) -> bool:
        pass

    @abstractmethod
    def handle(self, message: str) -> str:
        pass
