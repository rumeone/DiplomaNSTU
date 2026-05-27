"""Check if all numbers in a list are below a given threshold."""

from typing import List


def below_threshold(l: List[int], t: int) -> bool:
    """
    Check if all numbers in the list l are below threshold t.

    Args:
        l: List of integers to check.
        t: Threshold value.

    Returns:
        True if all numbers in l are below t, False otherwise.

    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    for num in l:
        if num >= t:
            return False
    return True