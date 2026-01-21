import pytest
from jar import Jar

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(2)
    jar.deposit(3)
    assert jar.size == 5

def test_withdraw():
    jar = Jar(6)
    jar.deposit(4)
    jar.withdraw(1)
    assert jar.size == 3


# extra tests

def test_default_capacity_and_size():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    assert str(jar) == ""

def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("five")

def test_invalid_deposit_and_withdraw():
    jar = Jar(5)

    with pytest.raises(ValueError):
        jar.deposit(-1)

    with pytest.raises(ValueError):
        jar.withdraw(-1)

    with pytest.raises(ValueError):
        jar.deposit(2.5)

    with pytest.raises(ValueError):
        jar.withdraw(1.1)

def test_over_capacity_deposit():
    jar = Jar(3)
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.deposit(2)

def test_over_withdraw():
    jar = Jar(3)
    jar.deposit(1)
    with pytest.raises(ValueError):
        jar.withdraw(2)
