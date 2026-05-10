import json
from Features.mapper import StepMapper
from Tests.ArgentinaForm.PlaywrightImpl import PArgentinaTest
from Tests.ArgentinaForm.SelenumMock import MArgentinaTest
from Utils import LoggerSingelton
from Utils.Consts import ARGENTINA_VALIDATE_KEYS
from Utils.TestUtils import build_scenario_groups


class Context:
    def __init__(self):
        self.mode = None
        self.action = None
        self.expect = None


def test_feature(feature_data, selenium_driver, playwright_page, mode):
    mapper = StepMapper()

    LoggerSingelton.printer("INFO", "TEST STARTED")

    errors = []

    try:
        pass_cases, empty_cases, invalid_cases = build_scenario_groups(
            filename="ArgentinaForm.json",
            validate_keys=ARGENTINA_VALIDATE_KEYS,
            mode=mode
        )

        LoggerSingelton.printer(
            "INFO",
            f"GROUPS LOADED | PASS={len(pass_cases)} EMPTY={len(empty_cases)} INVALID={len(invalid_cases)}"
        )

    except Exception as e:
        LoggerSingelton.printer("ERROR", f"FAILED BUILD GROUPS -> {e}")

    assert pass_cases and empty_cases and invalid_cases

    for scenario in feature_data:

        LoggerSingelton.printer(
            "INFO",
            f"RUNNING SCENARIO -> {scenario['name']}"
        )

        context = Context()
        try:
            for step in scenario["steps"]:
                LoggerSingelton.printer(
                    "INFO",
                    f"STEP -> {step}"
                )

                try:
                    mapper.execute(step, context)

                except Exception as e:
                    LoggerSingelton.printer(
                        "ERROR",
                        f"STEP FAILED -> {step} | {e}"
                    )

            LoggerSingelton.printer(
                "INFO",
                f"CONTEXT -> MODE={context.mode} ACTION={context.action} EXPECT={context.expect}"
            )

            cases_map = {
                "pass": pass_cases,
                "empty": empty_cases,
                "invalid": invalid_cases,
            }

            cases = cases_map.get(context.mode, [])

            LoggerSingelton.printer(
                "INFO",
                f"CASES COUNT -> {len(cases)}"
            )

            for index, case in enumerate(cases, start=1):

                LoggerSingelton.printer(
                    "INFO",
                    f"CASE [{index}] -> {json.dumps(case, ensure_ascii=False)}"
                )

                try:
                    LoggerSingelton.printer(
                        "INFO",
                        f"START SELENIUM [{context.mode.upper()}]"
                    )

                    MArgentinaTest(selenium_driver, case)

                    LoggerSingelton.printer(
                        "INFO",
                        "SELENIUM DONE"
                    )

                except Exception as e:
                    LoggerSingelton.printer(
                        "ERROR",
                        f"SELENIUM FAILED -> {e}"
                    )
                    errors.append(f"SELENIUM INIT FAILED | {str(e)}")

                try:

                    LoggerSingelton.printer(
                        "INFO",
                        f"START PLAYWRIGHT [{context.mode.upper()}]"
                    )

                    PArgentinaTest(playwright_page, case)

                    LoggerSingelton.printer(
                        "INFO",
                        f"PLAYWRIGHT PASSED [{context.mode.upper()}]"
                    )

                except Exception as e:

                    LoggerSingelton.printer(
                        "ERROR",
                        f"PLAYWRIGHT FAILED -> {e}"
                    )

                    errors.append(
                        f"PLAYWRIGHT FAILED | {scenario['name']} | CASE={case} | {str(e)}"
                    )

            assert context.mode
            assert context.action
            assert context.expect

            LoggerSingelton.printer(
                "INFO",
                f"SCENARIO PASSED -> {scenario['name']}"
            )

        except Exception as e:

            LoggerSingelton.printer(
                "ERROR",
                f"SCENARIO FAILED -> {scenario['name']} | {e}"
            )

            errors.append(
                f"FAILED -> {scenario['name']} | {str(e)}"
            )

    LoggerSingelton.printer(
        "INFO",
        f"TOTAL ERRORS -> {len(errors)}"
    )

    assert not errors, "\n".join(errors)

    LoggerSingelton.printer("INFO", "TEST FINISHED")
