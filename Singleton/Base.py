from abc import ABC, abstractmethod
from typing import Any, Optional


class BrowserDriver(ABC):

    @abstractmethod
    def get(self) -> Any:
        """Returns the live browser / page / driver instance"""
        pass

    @abstractmethod
    def quit(self) -> None:
        """Gracefully close the browser"""
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        pass


class SingletonMeta(type):
    _instances: dict[type, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]