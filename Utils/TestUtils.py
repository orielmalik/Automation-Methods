import json
import itertools
import itertools
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
JSON_DIR = PROJECT_ROOT / "Jsons"


def get_data_from_json(filename, generate_all_mixes):
    file_path = JSON_DIR / filename
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if generate_all_mixes:
        keys = data.keys()
        values = data.values()
        return [dict(zip(keys, combination)) for combination in itertools.product(*values)]

    return [{key: value[1] for key, value in data.items()}]
