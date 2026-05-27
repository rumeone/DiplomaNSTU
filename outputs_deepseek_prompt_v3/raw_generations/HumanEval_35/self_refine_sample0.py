"""
Module for finding the maximum element in a list of integers.
"""

from typing import List


def max_element(l: List[int]) -> int:
    """
    Return the maximum element in the list.
    Assume that the list is not empty.

    Example:
        >>> max_element([1, 2, 3])
        3
    """
    if not l:
        raise ValueError("List cannot be empty")

    max_value = l[0]
    for num in l[1:]:
        if num > max_value:
            max_value = num

    return max_value