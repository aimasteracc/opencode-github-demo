"""
Extended calculator module with additional mathematical functions.
"""

from calculator import add, subtract, multiply, divide, power, sqrt, modulo


def percentage(part: float, whole: float) -> float:
    """Calculate percentage: (part / whole) * 100
    
    Example:
        percentage(25, 100) = 25.0
        percentage(50, 200) = 25.0
    """
    if whole == 0:
        raise ValueError("Cannot calculate percentage with zero whole")
    return (part / whole) * 100


def absolute(value: float) -> float:
    """Calculate absolute value of a number."""
    return abs(value)


def maximum(*values: float) -> float:
    """Find the maximum value among given numbers.
    
    Example:
        maximum(1, 5, 3, 9, 2) = 9.0
    """
    if not values:
        raise ValueError("Cannot find maximum of empty values")
    return max(values)


def minimum(*values: float) -> float:
    """Find the minimum value among given numbers.
    
    Example:
        minimum(1, 5, 3, 9, 2) = 1.0
    """
    if not values:
        raise ValueError("Cannot find minimum of empty values")
    return min(values)


def average(*values: float) -> float:
    """Calculate the arithmetic mean of numbers.
    
    Example:
        average(1, 2, 3, 4, 5) = 3.0
    """
    if not values:
        raise ValueError("Cannot calculate average of empty values")
    return sum(values) / len(values)


def median(*values: float) -> float:
    """Calculate the median value of numbers.
    
    Example:
        median(1, 5, 3, 9, 2) = 3.0
        median(1, 5, 3, 9) = 4.0 (avg of 3 and 5)
    """
    if not values:
        raise ValueError("Cannot calculate median of empty values")
    
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    
    if n % 2 == 1:
        # Odd number of elements
        return float(sorted_values[mid])
    else:
        # Even number of elements
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2.0


def round_number(value: float, decimals: int = 2) -> float:
    """Round a number to specified decimal places.
    
    Args:
        value: The number to round
        decimals: Number of decimal places (default: 2)
    
    Example:
        round_number(3.14159, 2) = 3.14
        round_number(3.14159, 4) = 3.1416
    """
    return round(value, decimals)


def logarithm(value: float, base: float = 10) -> float:
    """Calculate logarithm of a value with specified base.
    
    Example:
        logarithm(100) = 2.0  (log10 of 100)
        logarithm(8, 2) = 3.0  (log2 of 8)
    """
    if value <= 0:
        raise ValueError("Cannot calculate logarithm of non-positive number")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")
    import math
    return math.log(value, base)


def factorial(value: int) -> int:
    """Calculate factorial of a non-negative integer.
    
    Example:
        factorial(5) = 120  (5 * 4 * 3 * 2 * 1)
        factorial(0) = 1
    """
    if value < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if value == 0:
        return 1
    
    result = 1
    for i in range(1, value + 1):
        result *= i
    return result


def is_prime(value: int) -> bool:
    """Check if a number is prime.
    
    Example:
        is_prime(7) = True
        is_prime(9) = False
    """
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    
    for i in range(3, int(value ** 0.5) + 1, 2):
        if value % i == 0:
            return False
    return True


if __name__ == "__main__":
    print("Extended Calculator Demo")
    print("=" * 50)
    
    # Original functions
    print("\n--- Original Functions ---")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")
    print(f"2 ^ 8 = {power(2, 8)}")
    print(f"sqrt(16) = {sqrt(16)}")
    print(f"10 % 3 = {modulo(10, 3)}")
    
    # New functions
    print("\n--- New Extended Functions ---")
    print(f"Percentage (25 of 100) = {percentage(25, 100)}%")
    print(f"Absolute value of -5 = {absolute(-5)}")
    print(f"Maximum of (1, 5, 3, 9, 2) = {maximum(1, 5, 3, 9, 2)}")
    print(f"Minimum of (1, 5, 3, 9, 2) = {minimum(1, 5, 3, 9, 2)}")
    print(f"Average of (1, 2, 3, 4, 5) = {average(1, 2, 3, 4, 5)}")
    print(f"Median of (1, 5, 3, 9, 2) = {median(1, 5, 3, 9, 2)}")
    print(f"Round 3.14159 to 2 decimals = {round_number(3.14159, 2)}")
    print(f"Log10 of 100 = {logarithm(100)}")
    print(f"Log2 of 8 = {logarithm(8, 2)}")
    print(f"Factorial of 5 = {factorial(5)}")
    print(f"Is 7 prime? {is_prime(7)}")
    print(f"Is 9 prime? {is_prime(9)}")
