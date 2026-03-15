from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Utils.Waiter import WaitFacade
from Utils.TestUtils import auto_error_logger


def get(selenium_driver, website):
    return selenium_driver.get(website)


@auto_error_logger
def MArgentinaTest(selenium_driver: WebDriver, data):
    get(selenium_driver, data[0]["website"])
    for key, value in data[0].items():
        if key not in ["website", "primary button"]:
            WaitFacade(selenium_driver).clickable((By.ID, key)).send_keys(value)
        elif key == "primary button":
            WaitFacade(selenium_driver).clickable((By.XPATH, value)).click()

    selenium_driver.close()
