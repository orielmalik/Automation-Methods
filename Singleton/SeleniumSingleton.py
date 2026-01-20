# autobrowser/selenium_driver.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .base import BrowserDriver, SingletonMeta


class SeleniumDriver(BrowserDriver, metaclass=SingletonMeta):
    def __init__(self, headless: bool = True, slow_mo: int = 0):
        self._driver: webdriver.Chrome | None = None
        self.headless = headless
        self.slow_mo = slow_mo

    def _lazy_init(self) -> None:
        if self._driver is None:
            options = Options()
            if self.headless:
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            if self.slow_mo > 0:
                options.add_experimental_option("prefs", {
                    "general.useragent.override": "Mozilla/5.0 (compatible; Automation)"
                })

            self._driver = webdriver.Chrome(options=options)

    def get(self) -> webdriver.Chrome:
        self._lazy_init()
        return self._driver

    def quit(self) -> None:
        if self._driver is not None:
            try:
                self._driver.quit()
            except:
                pass
            self._driver = None

    def is_initialized(self) -> bool:
        return self._driver is not None


# Convenience global access (most common usage pattern)
selenium = SeleniumDriver(headless=True)