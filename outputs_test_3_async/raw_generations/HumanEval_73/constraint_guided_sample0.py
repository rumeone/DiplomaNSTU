from typing import List


def smallest_change(arr: List[int]) -> int:
    """
    Return the minimum number of elements that need to be changed to make
    the array palindromic.

    A palindromic array reads the same forwards and backwards. In one change,
    one element can be changed to any other element.

    Args:
        arr: List of integers to check.

    Returns:
        Minimum number of changes required.

    Examples:
        >>> smallest_change([1, 2, 3, 5, 4, 7, 9, 6])
        4
        >>> smallest_change([1, 2, 3, 4, 3, 2, 2])
        1
        >>> smallest_change([1, 2, 3, 2, 1])
        0
    """
    changes = 0
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            changes += 1
        left += 1
        right -= 1

    return changes