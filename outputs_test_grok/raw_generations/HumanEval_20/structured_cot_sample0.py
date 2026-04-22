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
    closest = min(
        ((a, b) for a, b in zip(numbers, numbers[1:])),
        key=lambda pair: abs(pair[0] - pair[1])
    )
    return (min(closest), max(closest))