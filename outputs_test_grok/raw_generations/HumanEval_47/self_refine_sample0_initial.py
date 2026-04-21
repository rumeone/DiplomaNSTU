"""Compute the median of a list of numbers."""

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
        raise ValueError("median() arg should not be empty")

    sorted_list = sorted(l)
    n = len(sorted_list)
    mid = n // 2

    if n % 2 == 1:
        return sorted_list[mid]

    return (sorted_list[mid - 1] + sorted_list[mid]) / 2