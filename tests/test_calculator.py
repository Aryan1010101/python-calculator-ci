import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    # Test that the add function returns the correct sum.
    assert add(2, 3) == 5

def test_subtract():
    # Test that the subtract function returns the correct difference.
    assert subtract(5, 2) == 3

def test_multiply():
    # Test that the multiply function returns the correct product.
    assert multiply(3, 4) == 12

def test_divide():
    # Test that the divide function returns the correct quotient.
    assert divide(10, 2) == 5

def test_divide_by_zero():
    # Test that dividing by zero raises a ValueError.
    with pytest.raises(ValueError):
        divide(10, 0)
