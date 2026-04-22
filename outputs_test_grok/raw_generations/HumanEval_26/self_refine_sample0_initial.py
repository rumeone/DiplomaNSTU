"""Remove duplicates from a list while preserving order.

This module provides a function to remove all elements that occur more than
once from a list of integers, keeping the original order of the remaining
elements.
"""

from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all the elements that occur more than once.
    Keep the order of the elements the same as in the input.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    if not numbers:
        return []

    seen = set()
    duplicates = set()

    # First pass: identify all duplicates
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    # Second pass: keep only non-duplicates in original order
    return [num for num in numbers if num not in duplicates]