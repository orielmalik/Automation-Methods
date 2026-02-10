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
            options.add_argument("--disable-gpu")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self._driver = webdriver.Chrome(options=options)
        return self._driver

    def stop(self) -> None:
        if self._driver:
            self._driver.quit()
