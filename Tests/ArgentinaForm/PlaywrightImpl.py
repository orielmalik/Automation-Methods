from playwright.sync_api import Page

from Utils import LoggerSingelton
from Utils.Consts import byPlaywright
from Utils.TestUtils import auto_error_logger


def goto(playwright_page, website):
    playwright_page.goto(website)


def fill_field(playwright_page: Page, key: str, value):
    if key == "employees":
        playwright_page.select_option(byPlaywright["ID"](key), str(value))
    else:
        playwright_page.locator(byPlaywright["ID"](key)).fill(str(value))


def click(playwright_page: Page, selector):
    if isinstance(selector, dict):
        role = selector.get("role", "button")
        options = {k: v for k, v in selector.items() if k != "role"}
        playwright_page.get_by_role(role, **options).click()
    else:
        playwright_page.locator(selector).click()


@auto_error_logger
def task(playwright_page: Page, data):
    for key, value in ((k, v) for k, v in data[0].items() if k not in ["website", "primary button"]):
        LoggerSingelton.printer("INFO", f"Task {key}: {value}")
        fill_field(playwright_page, key, value)

    assert playwright_page.title() == "Example Form"


@auto_error_logger
def PArgentinaTest(playwright_page: Page, data, generate_all_mixes):
    LoggerSingelton.printer("INFO", "Starting PArgentinaTest")

    iterations = data if generate_all_mixes else [data[0]]
    LoggerSingelton.printer(
        "DEBUG",
        f"Generate all mixes: {generate_all_mixes} | Iterations: {len(iterations)}"
    )

    for index, current_data in enumerate(iterations, start=1):

        LoggerSingelton.printer(
            "INFO",
            f"Running iteration #{index}"
        )

        LoggerSingelton.printer(
            "DEBUG",
            f"Navigating to {current_data['website']}"
        )

        goto(playwright_page, current_data["website"])

        title = playwright_page.title()
        LoggerSingelton.printer("DEBUG", f"Page title: {title}")

        assert title == "Example Form", f"Unexpected title: {title}"

        for key, value in (
                (k, v) for k, v in current_data.items()
                if k not in ["website", "primary button"]
        ):
            LoggerSingelton.printer(
                "INFO",
                f"Filling field '{key}' with value '{value}'"
            )

            fill_field(playwright_page, key, value)

        primary = current_data["primary button"]

        LoggerSingelton.printer(
            "DEBUG",
            f"Primary button selector: {primary}"
        )

        LoggerSingelton.printer("INFO", "Clicking button via role selector")

        click(playwright_page, byPlaywright["XPATH"](primary))

        new_url = playwright_page.url
        LoggerSingelton.printer(
            "DEBUG",
            f"URL after click: {new_url}"
        )

        assert new_url != current_data["website"], \
            "URL did not change after clicking submit"

        if generate_all_mixes:
            LoggerSingelton.printer(
                "DEBUG",
                "Going back to form for next iteration"
            )
            playwright_page.go_back(wait_until="networkidle")

    LoggerSingelton.printer("INFO", "Finished PArgentinaTest")

    playwright_page.close()
