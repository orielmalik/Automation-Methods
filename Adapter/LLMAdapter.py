from abc import ABC, abstractmethod
from typing import Any


class LLMAdapter(ABC):

    def start(self) -> Any:
        pass

    def stop(self) -> None:
        pass

    def safe_call(self, messages, retries=3):
        pass