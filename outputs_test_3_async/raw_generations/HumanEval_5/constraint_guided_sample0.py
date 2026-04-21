"""Functions for inserting delimiters between list elements."""

from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers: The list of integers to process.
        delimeter: The integer to insert between consecutive elements.

    Returns:
        A new list with the delimiter inserted between consecutive elements.

    Example:
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []

    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)

    return result