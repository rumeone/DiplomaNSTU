"""Module providing list manipulation utilities."""

from typing import List


def incr_list(l: List[int]) -> List[int]:
    """
    Increment all elements of the list by 1.

    Args:
        l: List of integers to increment.

    Returns:
        New list with each element incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
    """
    return [x + 1 for x in l]