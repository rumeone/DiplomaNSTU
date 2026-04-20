from typing import List


def sort_even(l: List[int]) -> List[int]:
    """
    Return a list where odd indices remain unchanged, but values at even indices
    are sorted in ascending order.

    The function preserves the original values at odd indices while sorting only
    the values found at even indices (0, 2, 4, ...) and placing them back at
    even indices in sorted order.

    Args:
        l: A list of integers to be partially sorted.

    Returns:
        A new list with even-indexed values sorted and odd-indexed values unchanged.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    if not l:
        return []

    even_values = [l[i] for i in range(0, len(l), 2)]
    even_values.sort()

    result = l[:]
    for i, value in zip(range(0, len(l), 2), even_values):
        result[i] = value

    return result