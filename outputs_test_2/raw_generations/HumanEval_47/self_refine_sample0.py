from typing import List


def median(l: List[float]) -> float:
    """
    Return median of elements in the list l.

    The median is the middle value when the list is sorted.
    For lists with an even number of elements, the median is
    the average of the two middle values.

    Args:
        l: List of float values.

    Returns:
        The median value as a float.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        8.0
    """
    if not l:
        raise ValueError("Cannot compute median of empty list")

    sorted_list = sorted(l)
    length = len(sorted_list)
    middle_index = length // 2

    if length % 2 == 1:
        return float(sorted_list[middle_index])

    left_middle = sorted_list[middle_index - 1]
    right_middle = sorted_list[middle_index]
    return (left_middle + right_middle) / 2.0