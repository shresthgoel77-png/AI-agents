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
        raise ValueError("Division by zero is not allowed.")
    return a / b

def calculate_percentage(value: float, percentage: float) -> float:
    """Calculate the percentage of a given value."""
    return (value * percentage) / 100