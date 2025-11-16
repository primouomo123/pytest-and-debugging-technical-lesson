import pytest
from calculator import add, subtract, multiply, divide

def test_add():
	assert add(2, 3) == 5
	assert add(-1, 1) == 0

def test_subtract():
	assert subtract(10, 5) == 5
	assert subtract(0, 5) == -5

def test_multiply():
	assert multiply(4, 3) == 12
	assert multiply(-1, 5) == -5

def test_divide():
	assert divide(8, 2) == 4
    
    # Pytest can handle exceptions with "pytest.raises"
with pytest.raises(ZeroDivisionError):
    divide(5, 0)