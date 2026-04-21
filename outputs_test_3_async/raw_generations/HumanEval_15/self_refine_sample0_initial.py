"""
Module for generating sequences of numbers as formatted strings.
"""


def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers from 0 to n inclusive.

    Args:
        n: The upper bound of the sequence (inclusive).

    Returns:
        A space-separated string of numbers from 0 to n.
        If n is negative, returns an empty string.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    if n < 0:
        return ""

    numbers = [str(i) for i in range(n + 1)]
    return " ".join(numbers)