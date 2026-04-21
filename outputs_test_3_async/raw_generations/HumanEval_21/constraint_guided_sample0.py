"""Linear transformation of numeric lists to unit scale [0, 1]."""

from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Apply linear transformation to list so smallest becomes 0 and largest becomes 1.

    Args:
        numbers: List of at least two float numbers.

    Returns:
        Linearly transformed list scaled to [0, 1], or empty list for invalid input.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if not numbers or len(numbers) < 2:
        return []

    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        return [0.0] * len(numbers)

    scale = max_val - min_val
    return [(x - min_val) / scale for x in numbers]