import pytest
from Calculator import Calculator

@pytest.fixture
def calculator():
    cal = Calculator()
    return cal


def test_sum(calculator):
    a,b = 5,6
    assert 11 == calculator.sum(a,b)

def test_subt(calculator):
    a,b = 11,8
    assert 3 == calculator.subt(a,b)

def test_mul(calculator):
    a,b = 2,4
    assert 8 == calculator.mul(a,b)

def test_div(calculator):
    a,b = 9,3
    assert 3 == calculator.div(a,b)

    
