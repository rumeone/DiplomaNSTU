from typing import List


def unique(l: List[int]) -> List[int]:
    """
    Return sorted unique elements in a list.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert to set to remove duplicates, then sort
    return sorted(set(l))