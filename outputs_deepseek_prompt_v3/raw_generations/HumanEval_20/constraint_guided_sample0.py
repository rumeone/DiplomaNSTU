"""Find the two closest numbers in a list, preferring later pairs."""

from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Return the last two closest elements from a list.

    From a supplied list of numbers (of length at least two) select and return
    the last two elements that are the closest to each other and return them
    in order (smaller number, larger number).

    Args:
        numbers: A list of floats with at least two elements.

    Returns:
        A tuple containing the two closest numbers (smaller first, larger second),
        preferring later pairs when multiple pairs have the same minimal distance.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_distance = float('inf')
    best_pair = (numbers[0], numbers[1])

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if distance <= min_distance:
                min_distance = distance
                best_pair = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))

    return best_pair