import pytest

from Tests.Demoblaze.SelenumMock import MDemoblazeTest
from Utils import LoggerSingelton


def test_demoblaze(get_data, selenium_driver, playwright_page, generate_all_mixes):
    data_list = get_data("demoblaze.json")
    MDemoblazeTest(selenium_driver=selenium_driver, data=data_list)

