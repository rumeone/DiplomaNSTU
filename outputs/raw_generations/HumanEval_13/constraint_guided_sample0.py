def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b
    """
    # Ensure non-negative values for Euclidean algorithm
    x, y = abs(a), abs(b)
    while y:
        x, y = y, x % y
    return x