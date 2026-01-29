# base.py
from abc import ABC, abstractmethod
from typing import Any


class BrowserAdapter(ABC):

    @abstractmethod
    def start(self) -> Any:
        """Start browser and return driver/page"""
        pass

    @abstractmethod
    def stop(self) -> None:
        """Close browser cleanly"""
        pass
