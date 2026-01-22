# test_argentina_form.py
def test_argentina_form_data(get_data):
    data = get_data("ArgentinaForm.json")
    assert data is not None
    assert len(data) > 0


