"""Utility functions for list manipulation."""

from typing import List


def incr_list(l: List[int]) -> List[int]:
    """
    Increment all elements of the list by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
    """
    return [element + 1 for element in l]