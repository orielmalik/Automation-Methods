from playwright.sync_api import Page


def goto(playwright_page, website):
    playwright_page.goto(website)


def taskNot(playwright_page: Page
            , data):
    for key, value in data[0].items():
        if key == "employees":
            playwright_page.select_option(key, value)
            pass
        playwright_page.locator(key).fill(value)


def PArgentinaTest(playwright_page, data, generate_all_mixes):
    goto(playwright_page, data[0]["website"])
    assert playwright_page.title() == "Example Form"
    if not generate_all_mixes:
        taskNot(playwright_page, data)
