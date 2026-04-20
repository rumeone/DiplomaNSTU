from typing import List


def max_element(l: List[int]) -> int:
    """
    Return the maximum element in the list.
    Assume that the list is not empty.

    Example:
        >>> max_element([1, 2, 3])
        3
    """
    max_value = l[0]
    for num in l[1:]:
        if num > max_value:
            max_value = num
    return max_value