from typing import List


def sort_even(l: List[int]) -> List[int]:
    """
    Return a list where odd indices remain unchanged, but values at even indices
    are sorted in ascending order.

    Args:
        l: A list of integers.

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

    result = []
    even_index = 0
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_values[even_index])
            even_index += 1
        else:
            result.append(l[i])

    return result