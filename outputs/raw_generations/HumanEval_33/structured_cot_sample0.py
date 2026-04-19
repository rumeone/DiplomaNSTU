from typing import List


def sort_third(l: List[int]) -> List[int]:
    result = l[:]
    divisible_by_three = []
    positions = []
    
    for i, val in enumerate(l):
        if i % 3 == 0:
            divisible_by_three.append(val)
            positions.append(i)
    
    divisible_by_three.sort()
    
    for pos, sorted_val in zip(positions, divisible_by_three):
        result[pos] = sorted_val
    
    return result