"""
Utility to check if one integer is an integer power of another.
"""

def is_simple_power(x: int, n: int) -> bool:
    """Return True iff x equals n raised to some nonnegative integer power."""
    if x == 0 or n == 0:
        return False
    if x == 1:
        return True
    if n == 1:
        return False

    power = 1
    while power < x:
        power *= n
        if power == x:
            return True
    return False