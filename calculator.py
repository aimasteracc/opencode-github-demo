"""
Simple calculator module for demonstration.
"""

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Calculate base raised to the power of exponent."""
    return base ** exponent


def sqrt(number: float) -> float:
    """Calculate the square root of a number.
    
    Raises:
        ValueError: If number is negative.
    """
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return number ** 0.5


if __name__ == "__main__":
    print("Calculator Demo")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")
    print(f"2 ^ 8 = {power(2, 8)}")
    print(f"sqrt(16) = {sqrt(16)}")
