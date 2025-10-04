import pytest
from arithoperation import add, subtract, multiply, divide

def test_add():
    assert add(1, 2, 3) == 6
    assert add(-1, 1, 0) == 0
    assert add() == 0  # sum() of empty iterable = 0

def test_subtract():
    assert subtract(10, 2, 3) == 5
    assert subtract(5) == 5
    assert subtract() == 0

def test_multiply():
    assert multiply(2, 3, 4) == 24
    assert multiply(1, 0, 5) == 0
    assert multiply() == 1  # product of empty set = 1

def test_divide():
    assert divide(100, 2, 5) == 10
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    with pytest.raises(ValueError):
        divide()
