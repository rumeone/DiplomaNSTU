"""
Check if a number is a simple power of another number.
"""


def is_simple_power(x: int, n: int) -> bool:
    """
    Check if number x is a simple power of n.

    x is a simple power of n if n to the power of some integer equals x.

    Examples:
        is_simple_power(1, 4) => True (4^0 = 1)
        is_simple_power(2, 2) => True (2^1 = 2)
        is_simple_power(8, 2) => True (2^3 = 8)
        is_simple_power(3, 2) => False (only 2 and 4 are neighbouring simple powers)
        is_simple_power(3, 1) => False (1 is not a simple power of any number besides itself)
    """
    if n <= 0:
        return False

    if n == 1:
        return x == 1

    if x <= 0:
        return False

    if x == 1:
        return True

    current_power = n
    exponent = 1

    while current_power <= x:
        if current_power == x:
            return True
        current_power *= n
        exponent += 1

    return False