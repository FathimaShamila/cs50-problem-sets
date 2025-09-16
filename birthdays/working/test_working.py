import pytest
from working import convert

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_convert_error():
    invalid_inputs = ["12 AM 12 PM","8:70 AM to 6 PM"]
    for input_str in invalid_inputs:
        with pytest.raises(ValueError):
            convert(input_str)
