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
    # Handle edge cases: empty list or single element
    if len(numbers) < 2:
        return False

    # Sort the list to compare only adjacent elements
    sorted_numbers = sorted(numbers)

    # Check each adjacent pair
    for i in range(len(sorted_numbers) - 1):
        if abs(sorted_numbers[i] - sorted_numbers[i + 1]) < threshold:
            return True

    return False