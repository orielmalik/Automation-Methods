import sys
import os

import pytest

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, BASE_DIR)

from Features.parser import parse_feature
from Adapter.Playwrightadapter import PlaywrightAdapter
from Adapter.Seleniumadapter import SeleniumAdapter
from Utils import LoggerSingelton


def pytest_addoption(parser):
    parser.addoption(
        "--feature",
        action="store",
        default="ArgentinaForm"
    )

    parser.addoption(
        "--scenario",
        action="store",
        default=None
    )


# ---------------------------------------------------
# OPTIONAL GROQ FIXTURE
# ---------------------------------------------------
#
# @pytest.fixture(scope="session")
# def groq_service():
#
#     api_key = find_and_load_env(
#         "GROQ_SECRET_KEY"
#     )
#
#     LoggerSingelton.printer(
#         "INFO",
#         f"GROQ API LOADED -> {api_key[:15] if api_key else 'NOT FOUND'}"
#     )
#
#     adapter = GroqService(api_key)
#
#     adapter.start()
#
#     yield adapter
#
#     try:
#         adapter.stop()
#
#     except Exception as e:
#         LoggerSingelton.printer(
#             "ERROR",
#             f"GROQ STOP FAILED -> {e}"
#         )
#
# ---------------------------------------------------


@pytest.fixture(scope="session")
def feature_data(request):
    feature_name = request.config.getoption(
        "--feature"
    )

    scenario_filter = request.config.getoption(
        "--scenario"
    )

    LoggerSingelton.printer(
        "INFO",
        f"FEATURE -> {feature_name}"
    )

    scenarios = parse_feature(feature_name)

    if scenario_filter:
        LoggerSingelton.printer(
            "INFO",
            f"SCENARIO FILTER -> {scenario_filter}"
        )

        scenarios = [
            scenario
            for scenario in scenarios
            if scenario["name"] == scenario_filter
        ]

    LoggerSingelton.printer(
        "INFO",
        f"SCENARIOS LOADED -> {len(scenarios)}"
    )

    return scenarios


@pytest.fixture(scope="session")
def selenium_driver():
    adapter = SeleniumAdapter(headless=True)
    driver = adapter.start()
    yield driver
    adapter.stop()


@pytest.fixture(scope="session")
def playwright_page():
    adapter = PlaywrightAdapter(headless=False, slow_mo=500)
    page = adapter.start()
    yield page
    adapter.stop()


@pytest.fixture(scope="session")
def mode(request):
    selected = request.config.getoption(
        "--scenario"
    ) or "full"

    LoggerSingelton.printer(
        "INFO",
        f"MODE -> {selected}"
    )

    return selected
