"""Utility module for list filtering operations."""

from typing import List


def get_positive(numbers: List[int]) -> List[int]:
    """
    Return only the positive numbers in the list.

    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
    """
    return [number for number in numbers if number > 0]