from typing import List
from collections import Counter


def search(lst: List[int]) -> int:
    """
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    """
    # Count frequencies of all positive integers
    freq = Counter(lst)
    
    # Track the maximum valid integer found
    max_valid = -1
    
    # Check each integer and its frequency
    for num, count in freq.items():
        # Integer must be positive and frequency >= integer value
        if num > 0 and count >= num:
            if num > max_valid:
                max_valid = num
    
    return max_valid