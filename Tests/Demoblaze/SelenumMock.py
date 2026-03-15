from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utils.TestUtils import auto_error_logger
from Utils.Waiter import WaitFacade


def get(selenium_driver, website):
    return selenium_driver.get(website)


@auto_error_logger
def clickableUpperNavigator(selenium_driver: WebDriver, data):
    get(data[0]["website"])
    for item in data:
        if item not in ["STORE"]:
            WaitFacade(selenium_driver).clickable(By.XPATH, item.get("xpath")).click()
            get(data[0]["website"])
            WaitFacade(selenium_driver).text((By.XPATH, item.get("xpath")),item.get("text"))



    selenium_driver.close()


@auto_error_logger
def clickableProducts(selenium_driver: WebDriver, data):


@auto_error_logger
def MDemoblazeTest(selenium_driver: WebDriver, data):
    clickableUpperNavigator(selenium_driver, data["items"])

