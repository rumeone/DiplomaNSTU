"""
Module for checking if a number is a simple power of another number.
"""

def is_simple_power(x: int, n: int) -> bool:
    """
    Check if number x is a simple power of n.
    x is a simple power of n if n to the power of some integer equals x.
    """
    if n == 1:
        return x == 1
    if x == 1:
        return True
    if x < n:
        return False

    exponent = 0
    power = 1
    while power <= x:
        if power == x:
            return True
        exponent += 1
        power *= n
    return False