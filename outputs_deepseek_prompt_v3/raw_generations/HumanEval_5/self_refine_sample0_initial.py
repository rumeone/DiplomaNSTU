"""List manipulation utilities."""

from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers: List of integers to intersperse.
        delimeter: Integer to insert between consecutive elements.

    Returns:
        List with delimeter inserted between consecutive elements.

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