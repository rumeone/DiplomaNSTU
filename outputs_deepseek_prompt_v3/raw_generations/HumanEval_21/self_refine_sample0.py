"""Linear transformation of a list of numbers to the unit interval [0, 1]."""

from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Apply a linear transform to a list of numbers such that the smallest becomes 0
    and the largest becomes 1.

    Args:
        numbers: A list of floating-point numbers with at least two elements.

    Returns:
        A new list with the transformed values, or an empty list for invalid input.

    Examples:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if not numbers or len(numbers) < 2:
        return []

    min_val = min(numbers)
    max_val = max(numbers)

    # If all numbers are equal, transformation is undefined
    if max_val == min_val:
        return []

    # Apply linear transformation: (x - min) / (max - min)
    range_val = max_val - min_val
    return [(x - min_val) / range_val for x in numbers]