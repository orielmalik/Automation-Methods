from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utils.TestUtils import auto_error_logger


def get(selenium_driver, website):
    return selenium_driver.get(website)


@auto_error_logger
def MArgentinaTest(selenium_driver: WebDriver, data):
    get(selenium_driver, data[0]["website"])
    for key, value in data[0].items():
        if key not in ["website", "primary button"]:
            el = WebDriverWait(selenium_driver, 10).until(
                EC.element_to_be_clickable((By.ID, key))
            )
            el.send_keys(value)
        elif key == "primary button":
            button = WebDriverWait(selenium_driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, value))
            )
            button.click()

    selenium_driver.close()
