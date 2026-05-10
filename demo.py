import json

from Utils import LoggerSingelton
from Utils.TestUtils import build_scenario_groups

if __name__ == "__main__":

    from Utils.Consts import ARGENTINA_VALIDATE_KEYS

    LoggerSingelton.printer(
        "INFO",
        "RUNNING BUILD_SCENARIO_GROUPS DEMO"
    )

    try:

        pass_cases, empty_cases, invalid_cases = build_scenario_groups(
            filename="ArgentinaForm.json",
            validate_keys=ARGENTINA_VALIDATE_KEYS,
            mode="full"
        )

        LoggerSingelton.printer(
            "INFO",
            f"PASS COUNT -> {len(pass_cases)}"
        )

        for index, case in enumerate(pass_cases, start=1):

            LoggerSingelton.printer(
                "INFO",
                f"PASS [{index}] -> {json.dumps(case, ensure_ascii=False, indent=2)}"
            )

        LoggerSingelton.printer(
            "INFO",
            f"EMPTY COUNT -> {len(empty_cases)}"
        )

        for index, case in enumerate(empty_cases, start=1):

            LoggerSingelton.printer(
                "INFO",
                f"EMPTY [{index}] -> {json.dumps(case, ensure_ascii=False, indent=2)}"
            )

        LoggerSingelton.printer(
            "INFO",
            f"INVALID COUNT -> {len(invalid_cases)}"
        )

        for index, case in enumerate(invalid_cases, start=1):

            LoggerSingelton.printer(
                "INFO",
                f"INVALID [{index}] -> {json.dumps(case, ensure_ascii=False, indent=2)}"
            )

        LoggerSingelton.printer(
            "INFO",
            "DEMO FINISHED SUCCESSFULLY"
        )

    except Exception as e:

        LoggerSingelton.printer(
            "ERROR",
            f"DEMO FAILED -> {e}"
        )

        raise