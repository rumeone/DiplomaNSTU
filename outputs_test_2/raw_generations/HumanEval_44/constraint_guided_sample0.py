"""Convert an integer to its string representation in a given base (less than 10)."""


def change_base(x: int, base: int) -> str:
    """
    Convert integer x to a string representation in the specified base.

    The base must be less than 10. The function returns the string
    representation of x in the given base.

    Args:
        x: The integer to convert.
        base: The target base (must be less than 10).

    Returns:
        The string representation of x in the given base.

    Examples:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9.")

    if x == 0:
        return "0"

    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base

    return ''.join(reversed(digits))