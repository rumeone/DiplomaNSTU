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
        raise ValueError("List must contain at least two elements")

    min_distance = float('inf')
    closest_pair = (numbers[0], numbers[1])

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if distance < min_distance or (distance == min_distance and j > i):
                min_distance = distance
                if numbers[i] <= numbers[j]:
                    closest_pair = (numbers[i], numbers[j])
                else:
                    closest_pair = (numbers[j], numbers[i])

    return closest_pair