"""
Insert a delimiter between every pair of consecutive elements in a list.
"""

from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Example:
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    result = []
    for n in numbers:
        result.extend([n, delimeter])
    return result[:-1]