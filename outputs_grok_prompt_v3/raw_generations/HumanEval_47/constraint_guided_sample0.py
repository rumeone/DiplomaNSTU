"""Module providing a function to compute the median of a list of numbers."""

from typing import List


def median(l: List[float]) -> float:
    """
    Return median of elements in the list l.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        8.0
    """
    if not l:
        raise ValueError("Cannot compute median of empty list")
    sorted_values = sorted(l)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 1:
        return sorted_values[mid]
    return (sorted_values[mid - 1] + sorted_values[mid]) / 2