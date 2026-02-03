def goto(playwright_page, website):
    playwright_page.goto(website)


def PArgentinaTest(playwright_page, data, generate_all_mixes):
    goto(playwright_page, data[0]["website"])
