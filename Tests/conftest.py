# conftest.py
import pytest
from Utils.TestUtils import get_data_from_json


def pytest_addoption(parser):
    parser.addoption(
        "--generate-all-mixes",
        action="store_true"
    )


@pytest.fixture
def generate_all_mixes(request):
    return request.config.getoption("--generate-all-mixes")


@pytest.fixture
def get_data(generate_all_mixes):
    def _get_data(filename):
        return get_data_from_json(
            filename,
            generate_all_mixes
        )
    return _get_data
