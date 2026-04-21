"""Minimum changes to make an array palindromic.

This module provides a function to calculate the minimum number of element
changes required to make an array palindromic.
"""

from typing import List


def smallest_change(arr: List[int]) -> int:
    """Return minimum number of elements to change to make array palindromic.

    A palindromic array reads the same forwards and backwards. Each change
    allows modifying one element to any other value.

    Args:
        arr: List of integers to check.

    Returns:
        Minimum number of element changes required.

    Examples:
        >>> smallest_change([1, 2, 3, 5, 4, 7, 9, 6])
        4
        >>> smallest_change([1, 2, 3, 4, 3, 2, 2])
        1
        >>> smallest_change([1, 2, 3, 2, 1])
        0
    """
    changes = 0
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            changes += 1
        left += 1
        right -= 1

    return changes