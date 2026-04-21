"""Check if any two numbers in a list are closer than a given threshold."""

from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in a given list of numbers, there are any two numbers closer to each other than
    the given threshold.

    Args:
        numbers: List of floating-point numbers.
        threshold: Minimum distance threshold.

    Returns:
        True if any two numbers are closer than threshold, False otherwise.

    Examples:
        >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
        False
        >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
        True
    """
    if not numbers or len(numbers) < 2:
        return False

    sorted_numbers = sorted(numbers)

    for i in range(len(sorted_numbers) - 1):
        if abs(sorted_numbers[i] - sorted_numbers[i + 1]) < threshold:
            return True

    return False