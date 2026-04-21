"""
Module providing a function to check if a number is a simple power of another.
"""


def is_simple_power(x: int, n: int) -> bool:
    """
    Check if number x is a simple power of n.

    x is a simple power of n if n to the power of some integer equals x.
    For example:
        is_simple_power(1, 4) => true (4^0 = 1)
        is_simple_power(2, 2) => true (2^1 = 2)
        is_simple_power(8, 2) => true (2^3 = 8)
        is_simple_power(3, 2) => false (only 2 and 4 are neighbouring simple powers)
        is_simple_power(3, 1) => false (1 is not a simple power of any number besides itself)
    """
    if x == 1:
        return True
    if n == 1 or n == 0 or x <= 0:
        return False

    current = n
    while current < x:
        if current > (1 << 63) // n:  # Prevent integer overflow
            return False
        current *= n

    return current == x