import pytest

def test_argentina_form_data(
    get_data,
    browser,             # fixture - כבר מאותחל, יכול להיות Selenium או Playwright
    generate_all_mixes   # fixture שמגיע מה-CLI --generate-all-mixes
):
    # --- הצהרת נתונים ---
    data = get_data("ArgentinaForm.json")
    assert data, "JSON data must not be empty"

    assert browser is not None, "Browser driver must be initialized"
    assert isinstance(generate_all_mixes, bool), "generate_all_mixes must be boolean"

    # ---  SELENIUM ---


    # --- PLAYWRIGHT ---
