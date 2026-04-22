"""
Module providing utility function to check if a number is a simple power of another.
"""


def is_simple_power(x: int, n: int) -> bool:
    """
    Check if number x is a simple power of n.

    x is a simple power of n if n to the power of some integer equals x.

    Examples:
        is_simple_power(1, 4) => True   (4^0 = 1)
        is_simple_power(2, 2) => True   (2^1 = 2)
        is_simple_power(8, 2) => True   (2^3 = 8)
        is_simple_power(3, 2) => False
        is_simple_power(3, 1) => False
    """
    if x == 1:
        return True
    if n == 1:
        return False
    if x <= 0 or n <= 0:
        return False

    current = n
    while current < x:
        if current > x // n:
            return False
        current *= n

    return current == x