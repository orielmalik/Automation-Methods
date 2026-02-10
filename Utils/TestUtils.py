import json
import itertools
import itertools
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import os

from Utils import LoggerSingelton

max_workers = min(32, (os.cpu_count() or 1) + 4)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
JSON_DIR = PROJECT_ROOT / "Jsons"


def get_data_from_json(filename, generate_all_mixes, default_index=1):
    file_path = JSON_DIR / filename
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    normalized_data = {
        key: value if isinstance(value, list) else [value]
        for key, value in data.items()
    }

    if generate_all_mixes:
        keys = list(normalized_data.keys())
        values = list(normalized_data.values())
        return [
            dict(zip(keys, combination))
            for combination in itertools.product(*values)
        ]

    return [{
        key: values[default_index] if len(values) > default_index else values[0]
        for key, values in normalized_data.items()
    }]


def auto_error_logger(func):
    def wrapper(type, value, *args, **kwargs):
        try:
            return func(type, value, *args, **kwargs)
        except Exception as e:
            LoggerSingelton.printer("error", f"Automatic log of exception: {e}", exc_info=True)
            raise

    return wrapper


