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
        # According to the problem statement the list has length at least two,
        # but we guard against the empty or single-element case anyway.
        raise ValueError("List must contain at least two numbers")

    closest_pair = (numbers[0], numbers[1])
    min_diff = abs(numbers[1] - numbers[0])

    for i in range(1, len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[j] - numbers[i])
            if diff < min_diff or (diff == min_diff and j > 1):
                # We update on a strictly smaller difference, or on an equal
                # difference only when the new pair appears later in the list.
                # The condition "j > 1" ensures we prefer later pairs when
                # the first pair was the initial one.
                min_diff = diff
                closest_pair = (numbers[i], numbers[j])

    smaller, larger = sorted(closest_pair)
    return (smaller, larger)