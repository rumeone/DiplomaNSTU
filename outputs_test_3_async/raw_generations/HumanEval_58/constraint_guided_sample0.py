from typing import List


def common(l1: List[int], l2: List[int]) -> List[int]:
    """
    Return sorted unique common elements for two integer lists.

    Args:
        l1: First list of integers.
        l2: Second list of integers.

    Returns:
        A sorted list of unique integers that appear in both l1 and l2.

    Examples:
        >>> common([1, 4, 3, 34, 653, -2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    if not l1 or not l2:
        return []

    set1 = set(l1)
    set2 = set(l2)
    common_elements = set1.intersection(set2)

    return sorted(common_elements)