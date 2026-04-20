"""Linear transformation of numeric lists to unit scale."""

from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Apply linear transformation to a list so the smallest becomes 0 and largest becomes 1.

    Args:
        numbers: List of at least two floating-point numbers.

    Returns:
        Linearly transformed list where min becomes 0 and max becomes 1.
        Returns empty list for invalid inputs (None, too short, or all identical values).

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if numbers is None or len(numbers) < 2:
        return []

    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        return []

    value_range = max_val - min_val

    return [(x - min_val) / value_range for x in numbers]