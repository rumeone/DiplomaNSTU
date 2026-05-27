"""Module providing a function to extract sorted unique elements from a list."""

from typing import List


def unique(l: List[int]) -> List[int]:
    """
    Return sorted unique elements in a list.

    Args:
        l: List of integers from which to extract unique elements.

    Returns:
        List of sorted unique integers.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    if not l:
        return []

    unique_elements = list(set(l))
    unique_elements.sort()
    return unique_elements