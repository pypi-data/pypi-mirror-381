def add(*numbers):
    """Return the sum of all numbers."""
    return sum(numbers)

def subtract(*numbers):
    """Return the result of subtracting all following numbers from the first one."""
    if not numbers:
        return 0
    result = numbers[0]
    for n in numbers[1:]:
        result -= n
    return result

def multiply(*numbers):
    """Return the product of all numbers."""
    result = 1
    for n in numbers:
        result *= n
    return result

def divide(*numbers):
    """Return the result of dividing all numbers sequentially."""
    if not numbers:
        raise ValueError("At least one number is required")
    result = numbers[0]
    for n in numbers[1:]:
        if n == 0:
            raise ZeroDivisionError("Division by zero")
        result /= n
    return result
