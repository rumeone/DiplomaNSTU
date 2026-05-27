"""Linear transformation utilities for rescaling numeric data."""

from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Rescale a list of numbers to the unit interval [0, 1].

    Given a list of numbers (of at least two elements), apply a linear transform
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers: A list of floating-point numbers.

    Returns:
        A new list with the rescaled values, or an empty list for invalid input.

    Examples:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if not numbers or len(numbers) < 2:
        return []

    min_val = min(numbers)
    max_val = max(numbers)

    # Handle the case where all numbers are equal
    if max_val == min_val:
        return [0.0] * len(numbers)

    scale_factor = max_val - min_val
    return [(x - min_val) / scale_factor for x in numbers]