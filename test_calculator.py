import pytest
import mehth
from mehth import add, subtract, multiply, divide

def test_add_positive_numbers():
    assert mehth.add(6, 7) == 13