from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WaitFacade:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def all_present(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def text(self, locator, value):
        return self.wait.until(EC.text_to_be_present_in_element(locator, value))

    def value(self, locator, value):
        return self.wait.until(EC.text_to_be_present_in_element_value(locator, value))

    def frame(self, locator):
        return self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))

    def title(self, title):
        return self.wait.until(EC.title_is(title))

    def title_contains(self, value):
        return self.wait.until(EC.title_contains(value))

    def url(self, url):
        return self.wait.until(EC.url_to_be(url))

    def url_contains(self, value):
        return self.wait.until(EC.url_contains(value))

    def url_changes(self, old):
        return self.wait.until(EC.url_changes(old))

    def ready(self):
        return self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def click(self, locator):
        self.clickable(locator).click()

    def type(self, locator, text):
        el = self.visible(locator)
        el.clear()
        el.send_keys(text)

    def get(self, url):
        self.driver.get(url)
        self.ready()

    def element(self, locator):
        return self.visible(locator)

    def elements(self, locator):
        return self.all_present(locator)