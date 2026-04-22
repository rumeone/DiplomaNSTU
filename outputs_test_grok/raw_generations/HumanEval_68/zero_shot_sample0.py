from typing import List


def pluck(arr: List[int]) -> List[int]:
    if not arr:
        return []
    
    min_even = float('inf')
    min_index = -1
    
    for i, num in enumerate(arr):
        if num % 2 == 0 and num < min_even:
            min_even = num
            min_index = i
        elif num % 2 == 0 and num == min_even and i < min_index:
            min_index = i
    
    if min_index == -1:
        return []
    
    return [min_even, min_index]