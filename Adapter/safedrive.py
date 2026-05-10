class SafeDriver:
    def __init__(self, driver):
        self.driver = driver
        self.alive = True

    def get(self, url):
        try:
            return self.driver.get(url)
        except Exception as e:
            self.alive = False
            raise RuntimeError("SELENIUM_CRASH") from e

    def is_alive(self):
        try:
            _ = self.driver.title
            return True
        except:
            self.alive = False
            return False