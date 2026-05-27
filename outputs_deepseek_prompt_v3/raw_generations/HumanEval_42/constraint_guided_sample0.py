"""Module providing list manipulation utilities."""

from typing import List


def incr_list(l: List[int]) -> List[int]:
    """
    Increment all elements of the list by 1.

    Args:
        l: List of integers to increment.

    Returns:
        List of integers where each element is incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
    """
    return [element + 1 for element in l]