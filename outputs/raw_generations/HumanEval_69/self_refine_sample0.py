from typing import List
from collections import Counter


def search(lst: List[int]) -> int:
    """
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    """
    if not lst:
        return -1
    
    freq = Counter(lst)
    valid_numbers = [num for num, count in freq.items() 
                     if num > 0 and count >= num]
    
    return max(valid_numbers) if valid_numbers else -1