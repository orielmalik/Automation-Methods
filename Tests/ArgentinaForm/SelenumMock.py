import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from Utils import LoggerSingelton
from Utils.Waiter import WaitFacade
from Utils.TestUtils import auto_error_logger


def get(selenium_driver, website):
    return selenium_driver.get(website)


@auto_error_logger
def MArgentinaTest(selenium_driver: WebDriver, data):
    get(selenium_driver, data["website"])
    WaitFacade(selenium_driver).url( url=data["website"])
    WaitFacade(selenium_driver).title(title="Example Form")
    LoggerSingelton.printer("debug", selenium_driver.current_url)
    for key, value in data.items():
        if key not in ["website", "primary button","expected"]:
            WaitFacade(selenium_driver).clickable((By.ID, key)).send_keys(value)
        elif key == "primary button":
            WaitFacade(selenium_driver).clickable((By.XPATH, value)).click()

