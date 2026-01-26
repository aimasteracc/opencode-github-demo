"""
Test cases for extended calculator module.
"""

import pytest
from calculator_extended import (
    percentage, absolute, maximum, minimum, average,
    median, round_number, logarithm, factorial, is_prime
)


class TestPercentage:
    def test_percentage_simple(self):
        assert percentage(25, 100) == 25.0
    
    def test_percentage_fractional(self):
        assert percentage(50, 200) == 25.0
    
    def test_percentage_zero_whole_raises_error(self):
        with pytest.raises(ValueError, match="Cannot calculate percentage with zero whole"):
            percentage(25, 0)


class TestAbsolute:
    def test_absolute_positive(self):
        assert absolute(5) == 5
    
    def test_absolute_negative(self):
        assert absolute(-5) == 5
    
    def test_absolute_zero(self):
        assert absolute(0) == 0


class TestMaximum:
    def test_maximum_positive(self):
        assert maximum(1, 5, 3, 9, 2) == 9
    
    def test_maximum_negative(self):
        assert maximum(-1, -5, -3, -9, -2) == -1
    
    def test_maximum_single_value(self):
        assert maximum(42) == 42
    
    def test_maximum_empty_raises_error(self):
        with pytest.raises(ValueError, match="Cannot find maximum of empty values"):
            maximum()


class TestMinimum:
    def test_minimum_positive(self):
        assert minimum(1, 5, 3, 9, 2) == 1
    
    def test_minimum_negative(self):
        assert minimum(-1, -5, -3, -9, -2) == -9
    
    def test_minimum_single_value(self):
        assert minimum(42) == 42
    
    def test_minimum_empty_raises_error(self):
        with pytest.raises(ValueError, match="Cannot find minimum of empty values"):
            minimum()


class TestAverage:
    def test_average_positive(self):
        assert average(1, 2, 3, 4, 5) == 3.0
    
    def test_average_negative(self):
        assert average(-1, -2, -3) == -2.0
    
    def test_average_floats(self):
        assert average(1.5, 2.5, 3.5) == 2.5
    
    def test_average_empty_raises_error(self):
        with pytest.raises(ValueError, match="Cannot calculate average of empty values"):
            average()


class TestMedian:
    def test_median_odd_count(self):
        assert median(1, 5, 3, 9, 2) == 3.0
    
    def test_median_even_count(self):
        assert median(1, 5, 3, 9) == 4.0
    
    def test_median_single_value(self):
        assert median(42) == 42.0
    
    def test_median_empty_raises_error(self):
        with pytest.raises(ValueError, match="Cannot calculate median of empty values"):
            median()


class TestRoundNumber:
    def test_round_two_decimals(self):
        assert round_number(3.14159, 2) == 3.14
    
    def test_round_zero_decimals(self):
        assert round_number(3.14159, 0) == 3.0
    
    def test_round_four_decimals(self):
        assert round_number(3.14159, 4) == 3.1416
    
    def test_round_negative(self):
        assert round_number(-3.14159, 2) == -3.14


class TestLogarithm:
    def test_log10(self):
        assert logarithm(100) == 2.0
    
    def test_log2(self):
        assert logarithm(8, 2) == 3.0
    
    def test_log_custom_base(self):
        assert logarithm(27, 3) == 3.0
    
    def test_log_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot calculate logarithm of non-positive number"):
            logarithm(0)
    
    def test_log_negative_raises_error(self):
        with pytest.raises(ValueError, match="Cannot calculate logarithm of non-positive number"):
            logarithm(-10)
    
    def test_log_invalid_base_raises_error(self):
        with pytest.raises(ValueError, match="Base must be positive"):
            logarithm(10, 0)


class TestFactorial:
    def test_factorial_five(self):
        assert factorial(5) == 120
    
    def test_factorial_zero(self):
        assert factorial(0) == 1
    
    def test_factorial_one(self):
        assert factorial(1) == 1
    
    def test_factorial_ten(self):
        assert factorial(10) == 3628800
    
    def test_factorial_negative_raises_error(self):
        with pytest.raises(ValueError, match="Cannot calculate factorial of negative number"):
            factorial(-5)


class TestIsPrime:
    def test_prime_small(self):
        assert is_prime(2) == True
        assert is_prime(3) == True
        assert is_prime(5) == True
        assert is_prime(7) == True
    
    def test_not_prime(self):
        assert is_prime(4) == False
        assert is_prime(6) == False
        assert is_prime(8) == False
        assert is_prime(9) == False
    
    def test_prime_one(self):
        assert is_prime(1) == False
    
    def test_prime_negative(self):
        assert is_prime(-7) == False
    
    def test_prime_large_prime(self):
        assert is_prime(97) == True
    
    def test_prime_large_not_prime(self):
        assert is_prime(100) == False
