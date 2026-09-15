import pytest
from calculator import add, subtract, multiply, divide, calculate_percentage

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)

def test_calculate_percentage():
    
    assert calculate_percentage(750, 18) == 135.0