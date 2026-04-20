"""Linear transformation of a list to a unit scale."""

from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Apply a linear transform to a list of numbers such that the smallest
    becomes 0 and the largest becomes 1.

    Args:
        numbers: A list of at least two float numbers.

    Returns:
        A list of transformed numbers, or an empty list for invalid input.
    """
    if len(numbers) < 2:
        return []

    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        return []

    return [(x - min_val) / (max_val - min_val) for x in numbers]