byPlaywright = {
    "ID": lambda value: f"#{value}",
    "XPATH": lambda value: f"xpath={value}",
    "LINK_TEXT": lambda value: f"a:has-text('{value}')",
    "PARTIAL_LINK_TEXT": lambda value: f"a:has-text('{value}')",
    "NAME": lambda value: f'[name="{value}"]',
    "TAG_NAME": lambda value: value,
    "CLASS_NAME": lambda value: f".{value}",
    "CSS_SELECTOR": lambda value: value,
}
groqmodel = "llama-3.1-8b-instant"
FRAMEWORK_FIELDS = {
    "website",
    "primary button",
    "expected",
    "success selector",
    "success text",
    "expected url",
    "error selector",
    "error text"
}
CLASSIFICATION_PROMPT = """Classify this test case. Return ONLY JSON, no explanation.

Rules:
- "empty": ANY of {validate_keys} is ""
- "pass": ALL of {validate_keys} are non-empty and realistic
- "invalid": ALL non-empty but at least one is malformed

Case: {case}

{{"pass":[],"empty":[],"invalid":[]}}"""

ARGENTINA_VALIDATE_KEYS = ["name", "email", "phone", "company"]
