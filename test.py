import pytest
from Calculator import Calculator
from Student import Student

@pytest.fixture
def calculator():
    cal = Calculator()
    return cal

@pytest.fixture
def student():
    stu = Student("Santiago", "Martinez", 21, "Software Engineer")
    return stu


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

def test_getName(student):
    assert "Santiago" == student.name

def test_getLastName(student):
    assert "Martinez" == student.lastName

def test_getAge(student):
    assert 21 == student.age

def test_getCareer(student):
    assert "Software Engineer" == student.career

    
