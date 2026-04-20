"""
Module for checking if a list contains two distinct elements that sum to zero.
"""

from typing import List


def pairs_sum_to_zero(l: List[int]) -> bool:
    """
    Check if there are two distinct elements in the list that sum to zero.

    Args:
        l: A list of integers.

    Returns:
        True if there exist two distinct indices i and j such that
        l[i] + l[j] == 0, False otherwise.

    Examples:
        >>> pairs_sum_to_zero([1, 3, 5, 0])
        False
        >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
        True
    """
    seen = set()
    for num in l:
        complement = -num
        if complement in seen:
            return True
        seen.add(num)
    return False