from selenium.webdriver.common.by import By
byPlaywright = {
    "ID": lambda value: f"#{value}",
    "XPATH": lambda value: value,
    "LINK_TEXT": lambda value: f"a:has-text('{value}')",
    "PARTIAL_LINK_TEXT": lambda value: f"a:has-text('{value}')",
    "NAME": lambda value: f'[name="{value}"]',
    "TAG_NAME": lambda value: value,
    "CLASS_NAME": lambda value: f".{value}",
    "CSS_SELECTOR": lambda value: value,
}
bySelenium = {
    "ID": By.ID,
    "XPATH": By.XPATH,
    "LINK_TEXT": By.LINK_TEXT,
    "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
    "NAME": By.NAME,
    "TAG_NAME": By.TAG_NAME,
    "CLASS_NAME": By.CLASS_NAME,
    "CSS_SELECTOR": By.CSS_SELECTOR,
}