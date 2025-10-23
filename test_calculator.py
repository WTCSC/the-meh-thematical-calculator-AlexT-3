import pytest
from calculator import add, subtract, multiply, divide

def test_add_positive_numbers():
    assert add(6, 7) == 13

def test_add_negative_numbers():
    assert add(-3, -11) == -14

def test_subtract_two_numbers():
    assert subtract(20, 4) == 16

def test_subract_larger_num_from_smaller_num():
    assert subtract(6, 7) == -1

def test_multiply_positive_numbers():
    assert multiply(6, 7) == 42

def test_multiply_by_zero():
    assert multiply(10, 0) == 0

def test_divide_positive_numbers():
    assert divide (9, 3) == 3

def test_divide_by_one():
    assert divide (5, 1) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)