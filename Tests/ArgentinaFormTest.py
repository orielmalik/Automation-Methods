import pytest

from TestImpl.SelenimMock import ArgentinaTest


def test_argentina_form_data(
    get_data,
    selenium_driver,
    playwright_page,
    generate_all_mixes
):
    data = get_data("ArgentinaForm.json")
    ArgentinaTest(selenium_driver, data)


    # --- PLAYWRIGHT ---
    # playwright_run_tests(playwright_page, data, generate_all_mixes)
