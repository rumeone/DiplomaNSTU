"""Check for close numerical elements in lists."""

from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in a given list of numbers, there are any two numbers closer to each other than
    the given threshold.

    Examples:
        >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
        False
        >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
        True
    """
    sorted_numbers = sorted(numbers)
    for previous, current in zip(sorted_numbers, sorted_numbers[1:]):
        if current - previous < threshold:
            return True
    return False