"""Utility for performing circular digit shifts on integers."""

def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    digits = str(x)
    num_digits = len(digits)
    if shift > num_digits:
        return digits[::-1]
    effective_shift = shift % num_digits
    if effective_shift == 0:
        return digits
    return digits[-effective_shift:] + digits[:-effective_shift]