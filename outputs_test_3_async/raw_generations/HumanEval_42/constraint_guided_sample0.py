"""Module providing functions for list manipulation operations."""

from typing import List


def incr_list(l: List[int]) -> List[int]:
    """
    Increment all elements of the list by 1.

    Args:
        l: A list of integers to be incremented.

    Returns:
        A new list where each element is incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
    """
    if not l:
        return []

    return [element + 1 for element in l]