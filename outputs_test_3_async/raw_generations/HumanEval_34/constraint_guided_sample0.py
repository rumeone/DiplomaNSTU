from typing import List


def unique(l: List[int]) -> List[int]:
    """
    Return sorted unique elements in a list.

    Args:
        l: A list of integers.

    Returns:
        A sorted list containing only the unique elements from the input list.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    if not l:
        return []

    unique_elements = set(l)
    return sorted(unique_elements)