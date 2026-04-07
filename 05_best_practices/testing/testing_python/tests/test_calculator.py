import unittest

from src.calculator import sum, subtract, multiply, divide

class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        assert sum(2, 3) == 5

    def test_subtract(self):
        assert subtract(3, 2) == 1

    def test_multiply(self):
        assert multiply(3, 2) == 6

    def test_divide(self):
        assert divide(6, 2) == 3