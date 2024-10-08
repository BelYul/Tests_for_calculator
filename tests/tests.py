import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 9, 3) == 6

    def test_division_success(self):
        assert self.calc.division(self, 25, 5) == 5

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_multiply_success(self):
        assert self.calc.multiply(self, 4, 3) == 12

    def teardown(self):
        print('Выполение метода Teardown')