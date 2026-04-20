"""Module for removing duplicate elements from a list while preserving order."""

from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all the elements that occur more than once.
    Keep the order of the elements the same as in the input.

    Args:
        numbers: A list of integers.

    Returns:
        A new list containing only elements that appear exactly once in the
        original list, in the same order as they appeared.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    if not numbers:
        return []

    element_count = {}
    for num in numbers:
        element_count[num] = element_count.get(num, 0) + 1

    result = []
    for num in numbers:
        if element_count[num] == 1:
            result.append(num)

    return result