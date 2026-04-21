"""Module providing circular shift functionality for integer digits."""

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
    if x == 0:
        return "0"

    # Convert to string for easy digit manipulation
    digits = str(abs(x))
    num_digits = len(digits)

    # If shift is greater than number of digits, return reversed
    if shift >= num_digits:
        reversed_digits = digits[::-1]
        return reversed_digits if x >= 0 else "-" + reversed_digits

    # For right circular shift, we take the last 'shift' digits and move them to front
    effective_shift = shift % num_digits
    if effective_shift == 0:
        result = digits
    else:
        result = digits[-effective_shift:] + digits[:-effective_shift]

    # Add sign if original number was negative
    if x < 0:
        result = "-" + result

    return result