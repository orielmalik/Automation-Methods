from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from Adapter.Base import BrowserAdapter
import tempfile


class SeleniumAdapter(BrowserAdapter):
    def __init__(self, headless: bool = False):
        self.headless = headless
        self._driver: WebDriver | None = None

    def start(self) -> WebDriver:
        options = Options()

        if self.headless:
            options.add_argument("--headless=new")

        temp_profile = tempfile.mkdtemp()

        options.add_argument(f"--user-data-dir={temp_profile}")

        options.add_argument("--incognito")
        options.add_argument("--guest")

        options.add_argument("--disable-blink-features=AutomationControlled")

        options.add_argument("--disable-gpu")
        options.add_argument("--disable-software-rasterizer")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")

        options.add_argument("--disable-application-cache")
        options.add_argument("--disable-save-password-bubble")

        options.add_argument("--start-maximized")

        self._driver = webdriver.Chrome(options=options)

        self._driver.implicitly_wait(5)

        return self._driver

    def stop(self) -> None:
        if self._driver:
            self._driver.quit()