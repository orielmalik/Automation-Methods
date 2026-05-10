import requests
import time

from Utils import LoggerSingelton


class OpenRouterService:

    _instances = {}

    _instances = {}

    def __new__(
            cls,
            api_key: str,
            model: str ="openrouter/free"
    ):

        key = f"{api_key}:{model}"

        if key not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[key] = instance

        return cls._instances[key]
    def __init__(
        self,
        api_key: str,
        model: str = "openrouter/free"
    ):

        if getattr(self, "_initialized", False):
            return

        self.api_key = api_key
        self.model = model

        self.base_url = (
            "https://openrouter.ai/api/v1/chat/completions"
        )

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "AutomationMethods"
        }

        self._initialized = True

    def safe_openrouter_call(
        self,
        messages,
        retries=3
    ):

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0,
            "response_format": {
                "type": "json_object"
            }
        }

        for attempt in range(retries):

            try:

                response = requests.post(
                    self.base_url,
                    headers=self.headers,
                    json=payload,
                    timeout=120
                )

                if response.status_code == 429:

                    LoggerSingelton.printer(
                        "WARNING",
                        "Rate limit reached"
                    )

                    if attempt == retries - 1:
                        raise Exception(
                            "OpenRouter rate limit reached"
                        )

                    time.sleep(2 ** attempt)
                    continue

                if response.status_code >= 500:

                    LoggerSingelton.printer(
                        "ERROR",
                        f"Server Error: {response.text}"
                    )

                    raise Exception(
                        "OpenRouter internal server error"
                    )

                if response.status_code >= 400:

                    LoggerSingelton.printer(
                        "ERROR",
                        f"Bad Request: {response.text}"
                    )

                    raise Exception(
                        response.text
                    )

                return response.json()

            except requests.RequestException as e:

                LoggerSingelton.printer(
                    "ERROR",
                    f"OpenRouter Connection Error: {str(e)}"
                )

                if attempt == retries - 1:
                    raise Exception(
                        "OpenRouter connection failed"
                    )

                time.sleep(2 ** attempt)