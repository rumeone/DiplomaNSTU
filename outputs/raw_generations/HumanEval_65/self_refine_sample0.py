def circular_shift(x: int, shift: int) -> str:
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    digits = str(x)
    num_digits = len(digits)

    if shift > num_digits:
        return digits[::-1]

    split_point = num_digits - shift
    return digits[split_point:] + digits[:split_point]