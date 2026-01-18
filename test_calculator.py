"""
Test cases for calculator module.
"""

import pytest
from calculator import add, subtract, multiply, divide, power, sqrt


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        assert add(-2, 3) == 1

    def test_add_floats(self):
        assert add(2.5, 3.5) == 6.0


class TestSubtract:
    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_subtract_negative_numbers(self):
        assert subtract(-5, -3) == -2

    def test_subtract_mixed_numbers(self):
        assert subtract(-2, 3) == -5


class TestMultiply:
    def test_multiply_positive_numbers(self):
        assert multiply(2, 3) == 6

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_multiply_negative_numbers(self):
        assert multiply(-2, -3) == 6


class TestDivide:
    def test_divide_positive_numbers(self):
        assert divide(6, 3) == 2

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_divide_floats(self):
        assert divide(5, 2) == 2.5


class TestPower:
    def test_power_positive_exponent(self):
        assert power(2, 3) == 8

    def test_power_zero_exponent(self):
        assert power(5, 0) == 1

    def test_power_negative_exponent(self):
        assert power(2, -1) == 0.5

    def test_power_fractional_exponent(self):
        assert power(4, 0.5) == 2.0

    def test_power_large_exponent(self):
        assert power(2, 10) == 1024


class TestSqrt:
    def test_sqrt_positive_number(self):
        assert sqrt(16) == 4.0

    def test_sqrt_zero(self):
        assert sqrt(0) == 0.0

    def test_sqrt_fractional(self):
        assert sqrt(2.25) == 1.5

    def test_sqrt_one(self):
        assert sqrt(1) == 1.0

    def test_sqrt_negative_raises_error(self):
        with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
            sqrt(-1)

    def test_sqrt_large_number(self):
        assert sqrt(10000) == 100.0
