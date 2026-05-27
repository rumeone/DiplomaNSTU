from typing import List


def sort_even(l: List[int]) -> List[int]:
    """
    Return a list where odd indices remain unchanged and even indices are sorted.

    The function preserves values at odd positions (1, 3, 5, ...) and sorts the
    values at even positions (0, 2, 4, ...) in ascending order.

    Args:
        l: A list of integers.

    Returns:
        A new list with odd indices identical to l and even indices sorted.

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

    result = []
    for idx, value in enumerate(l):
        if idx % 2 == 0:
            result.append(even_values[idx // 2])
        else:
            result.append(value)

    return result