"""Module providing list filtering utilities."""

from typing import List


def get_positive(l: List[int]) -> List[int]:
    """
    Return only the positive numbers in the list.

    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
    """
    return [number for number in l if number > 0]