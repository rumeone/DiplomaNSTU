"""Circular digit shift utilities."""

def circular_shift(x: int, shift: int) -> str:
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Examples:
        >>> circular_shift(12, 1)
        "21"
        >>> circular_shift(12, 2)
        "12"
    """
    digit_string = str(x)
    num_digits = len(digit_string)

    if shift > num_digits:
        return digit_string[::-1]

    if shift == 0:
        return digit_string

    right_part = digit_string[-shift:]
    left_part = digit_string[:-shift]
    return right_part + left_part