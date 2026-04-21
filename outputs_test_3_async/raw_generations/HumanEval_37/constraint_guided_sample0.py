from typing import List


def sort_even(l: List[int]) -> List[int]:
    """
    Return a list where odd indices remain unchanged, but even indices are sorted.

    The function preserves the original values at odd positions while sorting the
    values at even positions (0, 2, 4, ...) in ascending order.

    Args:
        l: A list of integers.

    Returns:
        A new list with even-indexed values sorted and odd-indexed values unchanged.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, -1])
        [-1, 6, III, 4]
    """
    if not l:
        return []

    even_values = [l[i] for i in range(0, len(l), 2)]
    even_values.sort()

    result = l[:]
    for i, sorted_value in zip(range(0, len(l), 2), even_values):
        result[i] = sorted_value

    return result