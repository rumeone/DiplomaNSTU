"""Utility module for list operations."""

from typing import List


def common(l1: List[int], l2: List[int]) -> List[int]:
    """
    Return sorted unique common elements for two integer lists.

    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    first_set = set(l1)
    second_set = set(l2)
    common_elements = first_set.intersection(second_set)
    return sorted(common_elements)