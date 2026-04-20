"""
Module for checking if a number is a simple power of another number.
"""


def is_simple_power(x: int, n: int) -> bool:
    """
    Check if number x is a simple power of n.

    A number x is a simple power of n if there exists an integer exponent
    such that n raised to that exponent equals x.

    Args:
        x: The number to check.
        n: The base number.

    Returns:
        True if x is a simple power of n, False otherwise.

    Examples:
        >>> is_simple_power(1, 4)
        True
        >>> is_simple_power(8, 2)
        True
        >>> is_simple_power(3, 2)
        False
        >>> is_simple_power(3, 1)
        False
    """
    # Handle edge cases
    if n == 1:
        return x == 1  # Only 1 is a power of 1 (1^0 = 1, 1^1 = 1, etc.)

    if x == 1:
        return True  # n^0 = 1 for any n != 0

    if x <= 0 or n <= 0:
        return False

    # Check powers until we exceed x
    power = 1
    current = n

    while current <= x:
        if current == x:
            return True
        # Check for overflow
        if current > x // n:
            break
        current *= n

    return False