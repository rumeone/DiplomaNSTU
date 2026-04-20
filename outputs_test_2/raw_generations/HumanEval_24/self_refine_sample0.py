def largest_divisor(n: int) -> int:
    """
    Find the largest number that divides n evenly, smaller than n.
    Return -1 if such a number does not exist.

    Args:
        n: The integer to find the largest divisor for.

    Returns:
        The largest divisor of n that is less than n, or -1 if none exists.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(1)
        -1
        >>> largest_divisor(7)
        1
    """
    if n <= 1:
        return -1

    for divisor in range(n - 1, 0, -1):
        if n % divisor == 0:
            return divisor

    return -1