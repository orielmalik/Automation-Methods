import os

from Utils.TestUtils import find_file


def parse_feature(feature_name):
    if not feature_name.endswith(".feature"):
        filename = f"{feature_name}.feature"
    else:
        filename = feature_name

    path = find_file("Features", filename)
    scenarios = []
    current = None

    with open(path, "r", encoding="utf-8") as f:

        for line in f:

            line = line.strip()

            if line.startswith("Scenario:"):

                if current:
                    scenarios.append(current)

                current = {
                    "name": line.replace(
                        "Scenario:",
                        ""
                    ).strip(),

                    "steps": []
                }

            elif line.startswith(
                    ("Given", "When", "Then")
            ):

                if current is not None:
                    current["steps"].append(line)

        if current:
            scenarios.append(current)

    return scenarios
