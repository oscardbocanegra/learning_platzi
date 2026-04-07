def sum(a, b):
    """
    >>> sum(1, 2)
    3
    """

    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):

    """
    >>> divide(4, 2)
    Traceback (most recent call last):
    ValueError: Cannot divide by zero
    """
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b