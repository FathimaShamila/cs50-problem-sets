from jar import Jar
import pytest
def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    assert str(jar) == ""

def test_str():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    jar.withdraw(1)
    assert jar.size == 2


