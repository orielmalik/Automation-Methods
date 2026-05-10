import json
import itertools
import re
from pathlib import Path
import os
from Utils import LoggerSingelton
from functools import wraps
from Utils.LoggerSingelton import printer

ROOT = Path(__file__).parent.parent.absolute()
PROJECT_ROOT = Path(__file__).resolve().parent.parent
JSON_DIR = PROJECT_ROOT / "Jsons"

FIELD_RULES = {
    "email": r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$',
    "phone": r'^\+?[\d\s\-().]{7,15}$',
    "name": r"^[a-zA-Z\s'\-]{2,50}$",
    "company": r'^[\w\s\-&.]{2,50}$',
    "username": r'^[a-zA-Z0-9_]{3,20}$',
}


def classify_values(key, values, max_each=3):
    pattern = FIELD_RULES.get(key)
    result = {"pass": [], "empty": [], "invalid": []}

    for v in values:
        if v == "":
            if len(result["empty"]) < max_each:
                result["empty"].append(v)
        elif pattern:
            valid = bool(re.match(pattern, v)) and ".." not in v
            if valid and len(result["pass"]) < max_each:
                result["pass"].append(v)
            elif not valid and len(result["invalid"]) < max_each:
                result["invalid"].append(v)

    return result


def get_data_from_json(filename):
    file_path = JSON_DIR / filename
    with open(file_path, "r", encoding="utf-8") as file:
        raw = json.load(file)

    normalized = {
        k: v if isinstance(v, list) else [v]
        for k, v in raw.items()
    }

    keys = list(normalized.keys())
    values = list(normalized.values())

    cases = [
        dict(zip(keys, combo))
        for combo in itertools.product(*values)
    ]

    return cases, raw


def auto_error_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AssertionError as ae:
            LoggerSingelton.printer("error", f"Assertion failed: {ae}", exc_info=True)
            raise
        except Exception as e:
            LoggerSingelton.printer("error", f"Unhandled exception: {e}", exc_info=True)
            raise
    return wrapper


def get_root():
    try:
        current = Path(__file__).resolve()
    except Exception:
        current = Path.cwd()

    for parent in current.parents:
        if (parent / "Features").exists():
            return str(parent)

    raise Exception("ROOT not found")


def find_file(folder, filename):
    root = get_root()
    path = os.path.join(root, folder, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    return path


def build_scenario_groups(filename, validate_keys, mode="full"):

    _, raw_json = get_data_from_json(filename)

    MAX = 3

    classified = {}

    for key in validate_keys:

        values = raw_json.get(key, [])

        if not isinstance(values, list):
            values = [values]

        classified[key] = classify_values(
            key=key,
            values=values,
            max_each=MAX
        )

    def build_cases(category):

        key_values = []

        for key in validate_keys:

            vals = classified[key].get(category, [])

            if not vals:
                vals = [""]

            key_values.append(vals)

        cases = []

        for combo in itertools.product(*key_values):

            case = json.loads(json.dumps(raw_json))

            for key, value in zip(validate_keys, combo):
                case[key] = value

            cases.append(case)

            if len(cases) >= MAX:
                break

        return cases

    all_cases = {
        "pass": build_cases("pass"),
        "empty": build_cases("empty"),
        "invalid": build_cases("invalid"),
    }

    LoggerSingelton.printer(
        "INFO",
        f"SCENARIO GROUPS -> {json.dumps(all_cases, ensure_ascii=False)}"
    )

    if mode == "full":
        return (
            all_cases["pass"],
            all_cases["empty"],
            all_cases["invalid"]
        )

    return all_cases.get(mode, []), [], []