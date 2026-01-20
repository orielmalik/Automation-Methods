from playwright.sync_api import sync_playwright, BrowserContext, Page
from .base import BrowserDriver, SingletonMeta


class PlaywrightDriver(BrowserDriver, metaclass=SingletonMeta):
    def __init__(self, headless: bool = True, slow_mo: float = 0):
        self._playwright = None
        self._browser = None
        self._context: BrowserContext | None = None
        self._page: Page | None = None

        self.headless = headless
        self.slow_mo = slow_mo

    def _lazy_init(self):
        if self._page is None:
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

    def get(self) -> Page:
        self._lazy_init()
        return self._page

    def quit(self) -> None:
        if self._page is not None:
            try:
                self._context.close()
                self._browser.close()
                self._playwright.stop()
            except:
                pass
            self._page = self._context = self._browser = self._playwright = None

    def is_initialized(self) -> bool:
        return self._page is not None


playwright = PlaywrightDriver(headless=True, slow_mo=50)