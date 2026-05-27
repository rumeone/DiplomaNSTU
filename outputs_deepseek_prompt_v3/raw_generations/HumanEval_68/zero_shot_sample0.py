from typing import List

def pluck(arr: List[int]) -> List[int]:
    if not arr:
        return []
    
    smallest_even = None
    smallest_index = -1
    
    for i, num in enumerate(arr):
        if num % 2 == 0:
            if smallest_even is None or num < smallest_even or (num == smallest_even and i < smallest_index):
                smallest_even = num
                smallest_index = i
    
    if smallest_even is None:
        return []
    
    return [smallest_even, smallest_index]