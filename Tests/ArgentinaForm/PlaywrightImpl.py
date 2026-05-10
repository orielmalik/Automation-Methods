from playwright.sync_api import Page, expect
import re

from Utils.Consts import FRAMEWORK_FIELDS
from Utils import LoggerSingelton
from Utils.Consts import byPlaywright
from Utils.TestUtils import auto_error_logger


def goto(playwright_page: Page, website: str):
    playwright_page.goto(website, wait_until="networkidle")


def ensure_form_state(playwright_page: Page):
    expect(playwright_page.locator("form")).to_be_visible()


def wait_for_element(playwright_page: Page, selector, state="visible", timeout=10000):
    playwright_page.locator(selector).wait_for(
        state=state,
        timeout=timeout
    )


def handle_field(playwright_page: Page, key: str, value):
    locator = playwright_page.locator(byPlaywright["ID"](key))
    tag_name = locator.evaluate("(el) => el.tagName.toLowerCase()")

    if tag_name == "select":
        if isinstance(value, list):
            value = value[0]

        playwright_page.select_option(
            byPlaywright["ID"](key),
            value
        )
    else:
        locator.fill(str(value))


def click(playwright_page: Page, selector):
    LoggerSingelton.printer("debug", f"clicking  {selector}")
    playwright_page.locator(selector).click()


def validate_result(playwright_page: Page, current_data):
    expected = current_data.get("expected", "pass")

    if expected == "pass":
        success_selector = current_data.get("success selector")
        success_text = current_data.get("success text")
        expected_url = current_data.get("expected url")

        if success_selector:
            expect(playwright_page.locator(success_selector)).to_be_visible()

            if success_text:
                expect(playwright_page.locator(success_selector)).to_contain_text(success_text)

        if expected_url:
            expect(playwright_page).to_have_url(re.compile(expected_url))

    elif expected == "fail":
        error_selector = current_data.get("error selector")
        error_text = current_data.get("error text")

        expect(playwright_page.locator(error_selector)).to_be_visible()
        expect(playwright_page.locator(error_selector)).to_contain_text(error_text)


def submit_and_capture_response(playwright_page: Page, button_selector: str):
    response_status = None

    try:
        with playwright_page.expect_response(
                lambda response: "/submit" in response.url,
                timeout=8000
        ) as response_info:

            click(playwright_page, button_selector)

        response_status = response_info.value.status
        LoggerSingelton.printer("DEBUG", f"Response status: {response_status}")

    except Exception:
        LoggerSingelton.printer("DEBUG", "No /submit response intercepted")

    playwright_page.wait_for_load_state("domcontentloaded", timeout=15000)

    if response_status is not None:
        assert response_status == 200, f"Unexpected response status: {response_status}"

    return response_status


@auto_error_logger
def PArgentinaTest(playwright_page: Page, data):
    LoggerSingelton.printer("INFO", "Starting PArgentinaTest ")
    LoggerSingelton.printer("DEBUG", data)
    goto(playwright_page, data["website"])
    iterations = data if isinstance(data, list) else [data]
    total = len(iterations)
    for index, current_data in enumerate(iterations, start=1):
        LoggerSingelton.printer("INFO", f"Running iteration #{index}/{total}")
        try:
            title = playwright_page.title()
            assert title == "Example Form", f"Unexpected title: {title}"

            for key, value in (
                    (k, v) for k, v in current_data.items()
                    if k not in FRAMEWORK_FIELDS
            ):
                LoggerSingelton.printer("INFO", f"Handling field '{key}'")
                handle_field(playwright_page, key, value)
            primary = current_data["primary button"]
            wait_for_element(playwright_page, byPlaywright["XPATH"](primary))
            submit_and_capture_response(playwright_page, byPlaywright["XPATH"](primary))

            expected = current_data.get("expected", "pass")
            if expected == "fail":
                ensure_form_state(playwright_page)

            validate_result(playwright_page, current_data)

            LoggerSingelton.printer("INFO", f"Iteration #{index}/{total} completed successfully")
            playwright_page.goto(data["website"], wait_until="domcontentloaded")


        except Exception as e:
            LoggerSingelton.printer("ERROR", f"Iteration #{index}/{total} failed: {e}")
            raise

    LoggerSingelton.printer("INFO", "Finished PArgentinaTest")
