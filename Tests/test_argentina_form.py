from Tests.ArgentinaForm.PlaywrightImpl import PArgentinaTest
from Tests.ArgentinaForm.SelenumMock import MArgentinaTest

import pytest
from Utils import LoggerSingelton


def test_argentina_form_data(get_data, selenium_driver, playwright_page, generate_all_mixes):
    data_list = get_data("ArgentinaForm.json")
    errors = []
    for entry in data_list:
        try:
            MArgentinaTest(selenium_driver, [entry])
        except Exception as e:
            error_msg = f"Selenium failed for entry {entry}: {e}"
            LoggerSingelton.printer("ERROR", error_msg)
            errors.append(error_msg)

        try:
            PArgentinaTest(playwright_page, [entry], generate_all_mixes=False)
        except Exception as e:
            error_msg = f"Playwright failed for entry {entry}: {e}"
            LoggerSingelton.printer("ERROR", error_msg)
            errors.append(error_msg)

    if errors:
        pytest.fail("\n".join(errors))
