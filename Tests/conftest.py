import pytest
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from Adapter.Playwrightadapter import PlaywrightAdapter
from Adapter.Seleniumadapter import SeleniumAdapter
from Utils.TestUtils import get_data_from_json


def pytest_addoption(parser):
    parser.addoption(
        "--generate-all-mixes",
        action="store_true",
        default=False,
        help="Generate all data combinations instead of minimal set"
    )


@pytest.fixture(scope="session")
def generate_all_mixes(request):
    return request.config.getoption("--generate-all-mixes")


@pytest.fixture(scope="session")
def selenium_driver():
    adapter = SeleniumAdapter(headless=True)
    driver = adapter.start()
    yield driver
    adapter.stop()


@pytest.fixture(scope="session")
def playwright_page():
    adapter = PlaywrightAdapter(headless=True, slow_mo=50)
    page = adapter.start()
    yield page
    adapter.stop()


@pytest.fixture
def get_data(generate_all_mixes):
    def _get_data(filename):
        return get_data_from_json(
            filename=filename,
            generate_all_mixes=generate_all_mixes
        )
    return _get_data
