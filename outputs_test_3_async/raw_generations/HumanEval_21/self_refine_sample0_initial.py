from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    Return an empty list for any undefined edge cases.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if not numbers or len(numbers) < 2:
        return []

    min_value = min(numbers)
    max_value = max(numbers)

    if min_value == max_value:
        return [0.0] * len(numbers)

    return [(x - min_value) / (max_value - min_value) for x in numbers]