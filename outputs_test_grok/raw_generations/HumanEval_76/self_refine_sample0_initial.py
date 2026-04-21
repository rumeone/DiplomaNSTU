"""
Module providing a function to check if a number is a simple power of another.
"""


def is_simple_power(x: int, n: int) -> bool:
    """
    Check if number x is a simple power of n.

    x is a simple power of n if n to the power of some integer equals x.

    Examples:
        is_simple_power(1, 4) => True (4^0 = 1)
        is_simple_power(2, 2) => True (2^1 = 2)
        is_simple_power(8, 2) => True (2^3 = 8)
        is_simple_power(3, 2) => False
        is_simple_power(3, 1) => False
    """
    # Handle edge cases first
    if x == 1:
        # Any n^0 = 1, but 1 is not a simple power of 1
        return n != 1

    if n == 1:
        # 1 to any power is 1, so only x=1 would work (handled above)
        return False

    if x <= 0 or n <= 0:
        # Negative numbers and zero are not considered simple powers in this context
        return False

    # Repeatedly divide x by n while it's divisible
    current = x
    while current > 1:
        if current % n != 0:
            return False
        current = current // n

    # If we reached exactly 1, then x was a power of n
    return current == 1