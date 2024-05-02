import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_saccess(self):
        assert self.calc.adding(self,1,1)==2

    def test_subtraction_saccess(self):
        assert self.calc.subtraction(self,1,1)==0

    def test_division_saccess(self):
        assert self.calc.division(self,1,1)==1

    def test_multiply_saccess(self):
        assert self.calc.multiply(self,1,1)==1

   # def test_adding_unsaccess(self):
        #assert self.calc.adding(self, 1, 1) == 3

    def test_zero_devision(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def tearDown(self):
        print('ВЫполнение метода TearDown')