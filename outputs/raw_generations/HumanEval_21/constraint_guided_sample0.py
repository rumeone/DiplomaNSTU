from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    Return an empty list for any undefined edge cases.
    """
    if not numbers or len(numbers) < 2:
        return []
    
    min_val = min(numbers)
    max_val = max(numbers)
    
    # If all numbers are equal, scaling is undefined
    if max_val == min_val:
        return []
    
    scale_factor = max_val - min_val
    return [(x - min_val) / scale_factor for x in numbers]