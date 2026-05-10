from groq import Groq, RateLimitError, APIStatusError

from Adapter.LLMAdapter import LLMAdapter
from Utils import LoggerSingelton
from Utils.Consts import groqmodel
from Utils.Errors import *

class GroqService(LLMAdapter):
    _instances = {}

    def __new__(cls, api_key: str):
        if api_key not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[api_key] = instance
        return cls._instances[api_key]

    def __init__(self, api_key: str):
        if getattr(self, "_initialized", False):
            return

        self.api_key = api_key
        self.client = None
        self._initialized = True

    def start(self):
        self.client = Groq(api_key=self.api_key)  # תמיד יוצר client חדש
        return self.client

    def stop(self):
        self.client = None
        GroqService._instances.pop(self.api_key, None)
        self._initialized = False

    def safe_call(self, messages, retries=3):
        if not self.client:
            self.start()

        last_error = None

        for attempt in range(retries):
            try:
                LoggerSingelton.printer("INFO", f"GROQ ATTEMPT {attempt + 1}")

                response = self.client.chat.completions.create(
                    model=groqmodel,
                    messages=messages,
                    timeout=30,
                    max_tokens=5990

                )
                return response.choices[0].message.content

            except RateLimitError as e:
                LoggerSingelton.printer("ERROR", f"RATE LIMIT -> {e}")
                last_error = GroqErrorHandler.handle(e)
                raise last_error

            except APIStatusError as e:
                LoggerSingelton.printer("ERROR", f"API STATUS -> {e}")
                last_error = GroqErrorHandler.handle(e)
                raise last_error
