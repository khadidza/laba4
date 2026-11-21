import pytest
from calculator import Calculator
@pytest.fixture
def calculator():
  return Calculator()
def test_add(calculator):
  assert calculator.add(2, 3) == 5
def test_subs(calculator):
  assert calculator.add(10, 4) == 6
def test_multi(calculator):
  assert calculator.add(3, 5) == 15
def test_divide(calculator):
  assert calculator.add(12, 3) == 4
def test_divide_zero(calculator):
  with pytest.raises(ValueError):
    calculator.divide(10, 0)
@pytest.mark.parametrize(
  "a, b, expected", 
  [
    (2.5, 4, 10.0)
    (-3, 2, -6.0)
  ],
)
def test_multipl_calc(calculator, a, b, expected):
  assert calculator.divide(a, b) == pytest.appox(expected) 

