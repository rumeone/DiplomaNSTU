"""Module providing a function to find the two closest numbers in a list."""

from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return
    the last two elements that are the closest to each other and return them
    in order (smaller number, larger number).

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    if len(numbers) < 2:
        # According to the docstring we assume at least two elements,
        # but guard clause for robustness.
        raise ValueError("List must contain at least two numbers")

    closest_pair = (numbers[0], numbers[1])
    min_diff = abs(numbers[1] - numbers[0])

    for i in range(1, len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[j] - numbers[i])
            if diff < min_diff or (diff == min_diff and j > 1):
                # Update when we find a smaller difference, or when we find
                # an equal difference that appears later in the list.
                # The "j > 1" condition ensures we prefer later pairs when
                # differences are equal, matching the "last two elements"
                # requirement.
                min_diff = diff
                smaller = min(numbers[i], numbers[j])
                larger = max(numbers[i], numbers[j])
                closest_pair = (smaller, larger)

    return closest_pair