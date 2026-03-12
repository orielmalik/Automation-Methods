from Tests.ArgentinaForm.PlaywrightImpl import PArgentinaTest
from Tests.ArgentinaForm.SelenimMock import MArgentinaTest


def test_argentina_form_data(
    get_data,
    selenium_driver,
    playwright_page,
    generate_all_mixes
):
    data = get_data("ArgentinaForm.json")
    MArgentinaTest(selenium_driver, data)
    PArgentinaTest(playwright_page, data,generate_all_mixes)
