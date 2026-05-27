"""Utility module for list operations."""

from typing import List


def max_element(numbers: List[int]) -> int:
    """
    Return the maximum element in the list.
    Assume that the list is not empty.

    Example:
        >>> max_element([1, 2, 3])
        3
    """
    current_max = numbers[0]
    for number in numbers[1:]:
        current_max = max(current_max, number)
    return current_max