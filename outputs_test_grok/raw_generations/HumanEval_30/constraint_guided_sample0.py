"""Filter positive integers from a list.

This module provides a simple utility function to extract positive numbers
from a list of integers.
"""


from typing import List


def get_positive(l: List[int]) -> List[int]:
    """
    Return only the positive numbers in the list.

    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
    """
    return [num for num in l if num > 0]