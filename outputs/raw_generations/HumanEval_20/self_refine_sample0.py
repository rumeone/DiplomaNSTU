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
        raise ValueError("Input list must contain at least two numbers")

    min_distance = float('inf')
    result = (0.0, 0.0)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if distance < min_distance:
                min_distance = distance
                if numbers[i] <= numbers[j]:
                    result = (numbers[i], numbers[j])
                else:
                    result = (numbers[j], numbers[i])
            elif distance == min_distance:
                # For equal distance, choose the pair with larger indices
                if numbers[i] <= numbers[j]:
                    current_pair = (numbers[i], numbers[j])
                else:
                    current_pair = (numbers[j], numbers[i])
                # Update only if this pair appears later in the list
                if j > result[1]:
                    result = current_pair

    return result