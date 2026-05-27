"""Remove duplicates from lists while preserving order of unique elements."""

from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all the elements that occur more than once.
    Keep the order of the elements the same as in the input.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    return [number for number in numbers if frequency[number] == 1]