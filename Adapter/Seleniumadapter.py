# selenium_adapter.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from Adapter.Base import BrowserAdapter


class SeleniumAdapter(BrowserAdapter):

    def __init__(self, headless: bool = False):
        self.headless = headless
        self._driver: WebDriver | None = None

    def start(self) -> WebDriver:
        options = Options()

        if self.headless:
            options.add_argument("--headless=new")

        # Prevent GPU / DirectComposition errors
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-software-rasterizer")

        # CI / Docker stability
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Optional stability flags
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")

        self._driver = webdriver.Chrome(options=options)
        return self._driver

    def stop(self) -> None:
        if self._driver:
            self._driver.quit()