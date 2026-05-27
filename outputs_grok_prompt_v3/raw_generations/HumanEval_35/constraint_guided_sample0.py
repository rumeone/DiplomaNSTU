"""Provide a function to return the maximum element from a list of integers."""

from typing import List


def max_element(l: List[int]) -> int:
    """
    Return the maximum element in the list.
    Assume that the list is not empty.

    Example:
        >>> max_element([1, 2, 3])
        3
    """
    maximum_element = l[0]
    for current_element in l[1:]:
        if current_element > maximum_element:
            maximum_element = current_element
    return maximum_element