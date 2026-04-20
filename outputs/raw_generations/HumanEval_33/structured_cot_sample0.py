from typing import List


def sort_third(l: List[int]) -> List[int]:
    result = l[:]
    divisible_by_three = []
    indices = []
    
    for i, val in enumerate(l):
        if i % 3 == 0:
            divisible_by_three.append(val)
            indices.append(i)
    
    divisible_by_three.sort()
    
    for idx, sorted_val in zip(indices, divisible_by_three):
        result[idx] = sorted_val
    
    return result