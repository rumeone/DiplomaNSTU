"""Module providing a function to calculate the median of a list of numbers."""

from typing import List


def median(l: List[float]) -> float:
    """Return median of elements in the list l.

    Args:
        l: List of numbers.

    Returns:
        The median value.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        8.0
    """
    if not l:
        raise ValueError("Cannot compute median of empty list")

    sorted_list = sorted(l)
    length = len(sorted_list)
    middle = length // 2

    if length % 2 == 1:
        return float(sorted_list[middle])
    else:
        left = sorted_list[middle - 1]
        right = sorted_list[middle]
        return (left + right) / 2.0