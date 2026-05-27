"""Utility module for list operations including element interspersion."""

from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Example:
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if len(numbers) <= 1:
        return list(numbers)

    result: List[int] = []
    for index, value in enumerate(numbers):
        if index > 0:
            result.append(delimeter)
        result.append(value)
    return result