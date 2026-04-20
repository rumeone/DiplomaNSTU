"""Module for sorting even-indexed elements in a list while preserving odd-indexed elements."""

from typing import List


def sort_even(l: List[int]) -> List[int]:
    """
    Return a list where odd indices are unchanged, but even indices are sorted.

    The function preserves elements at odd indices (1, 3, 5, ...) while sorting
    the elements at even indices (0, 2, 4, ...) in ascending order.

    Args:
        l: A list of integers to be partially sorted.

    Returns:
        A new list with even-indexed elements sorted and odd-indexed elements unchanged.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    if not l:
        return []

    # Extract and sort even-indexed elements
    even_elements = [l[i] for i in range(0, len(l), 2)]
    sorted_even = sorted(even_elements)

    # Reconstruct the list
    result = []
    sorted_index = 0
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(sorted_even[sorted_index])
            sorted_index += 1
        else:
            result.append(l[i])

    return result