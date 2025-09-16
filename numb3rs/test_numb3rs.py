from numb3rs import validate
def test_validate_numbers():
    assert validate("127.0.0.1") == True
    assert validate("256.255.255.255") == False
    assert validate("8.8.8") == False
    assert validate("255.255.255.255.1") == False
    assert validate("1.256.257.258") == False
def test_validate_strings():
    assert validate("cat") == False



