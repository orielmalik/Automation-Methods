from playwright.sync_api import Page

from Utils import LoggerSingelton
from Utils.Consts import byPlaywright
from Utils.TestUtils import auto_error_logger


def goto(playwright_page, website):
    playwright_page.goto(website)


@auto_error_logger
def taskNot(playwright_page: Page, data):
    for key, value in ((k, v) for k, v in data[0].items() if k != "website"):
        if key == "employees":
            playwright_page.select_option(byPlaywright["ID"](key), str(value))
        else:
            playwright_page.locator(byPlaywright["ID"](key)).fill(str(value))

    assert playwright_page.title() != "Example Form"

def PArgentinaTest(playwright_page: Page, data, generate_all_mixes):
    goto(playwright_page, data[0]["website"])
    assert playwright_page.title() == "Example Form"
    LoggerSingelton.printer("debug", playwright_page.title())
    if not generate_all_mixes:
        taskNot(playwright_page, data)
        playwright_page.locator("primary button").click()
        assert str(playwright_page.url()) != str(data[0]["website"])
        LoggerSingelton.printer("debug", "V click by locatorCLASS_NAME")
        playwright_page.go_back(wait_until="networkidle")
        taskNot(playwright_page, data)
        playwright_page.get_by_role("button", name=data[0]["primary button"]).click()
        assert str(playwright_page.url()) != str(data[0]["website"])

