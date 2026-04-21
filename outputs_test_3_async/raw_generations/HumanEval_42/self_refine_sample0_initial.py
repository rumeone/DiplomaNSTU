"""List manipulation utilities."""

from typing import List


def incr_list(l: List[int]) -> List[int]:
    """
    Increment all elements of the list by 1.

    Args:
        l: A list of integers.

    Returns:
        A new list with each element incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
    """
    if not l:
        return []

    return [x + 1 for x in l]