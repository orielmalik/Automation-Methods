# playwright_adapter.py
from playwright.sync_api import sync_playwright, BrowserContext, Page
from Adapter.Base import BrowserAdapter


class PlaywrightAdapter(BrowserAdapter):

    def __init__(self, headless: bool = True, slow_mo: float = 0):
        self.headless = headless
        self.slow_mo = slow_mo

        self._playwright = None
        self._browser = None
        self._context: BrowserContext | None = None
        self._page: Page | None = None

    def start(self) -> Page:
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(
            headless=self.headless,
            slow_mo=self.slow_mo
        )
        self._context = self._browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 Automation"
        )
        self._page = self._context.new_page()
        return self._page

    def stop(self) -> None:
        if self._context:
            self._context.close()
        if self._browser:
            self._browser.close()
        if self._playwright:
            self._playwright.stop()
