"""
Check if a number is a simple power of another number.
"""


def is_simple_power(x: int, n: int) -> bool:
    """
    Check if number x is a simple power of n.

    A simple power means there exists an integer exponent such that n^exponent = x.

    Args:
        x: The number to check.
        n: The base to check against.

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
    # Edge cases
    if n <= 0 or x <= 0:
        return False

    if n == 1:
        return x == 1

    # Start from exponent 0 and increase until n^exponent >= x
    exponent = 0
    power = 1

    while power <= x:
        if power == x:
            return True
        exponent += 1
        power *= n

    return False