import pytest
from calculator import add, subtract, multiply, divide, power

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_power():
    assert power(2, 3) == 8      # 2³ = 8
    assert power(5, 2) == 25     # 5² = 25
    assert power(10, 0) == 1     # Any number to power 0 = 1
    assert power(3, 4) == 81     # 3⁴ = 81
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)