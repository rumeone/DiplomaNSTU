"""Utility functions for list operations."""

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
    if not l1 or not l2:
        return []

    # Use sets for O(1) lookups and automatic uniqueness
    set1 = set(l1)
    set2 = set(l2)

    # Find intersection and convert back to sorted list
    common_elements = sorted(set1 & set2)
    return common_elements