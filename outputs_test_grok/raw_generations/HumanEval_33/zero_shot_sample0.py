from typing import List


def sort_third(l: List[int]) -> List[int]:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.

    Examples:
        >>> sort_third([1, 2, 3])
        [1, 2, 3]
        >>> sort_third([5, 6, 3, 4, 8, 9, 2])
        [2, 6, 3, 4, 8, 9, 5]
    """
    # Extract values at indices divisible by 3
    third_values = [l[i] for i in range(len(l)) if i % 3 == 0]
    # Sort these values
    third_values.sort()
    
    # Create result list
    result = l[:]
    # Replace values at indices divisible by 3 with sorted values
    idx = 0
    for i in range(len(result)):
        if i % 3 == 0:
            result[i] = third_values[idx]
            idx += 1
    
    return result