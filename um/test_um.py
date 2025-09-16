from um import count
def test_count_um():
    assert count("um, hello world") == 1
    assert count("yummy") == 0
    assert count("hello, UM") == 1
