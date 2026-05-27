from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    """
    Determine if an object will fly based on balance and weight constraints.
    
    The object will fly if:
    1. It is balanced (palindromic list when ignoring trailing zeros)
    2. The sum of its elements is <= maximum weight w
    
    Args:
        q: List of non-negative integers representing the object
        w: Maximum possible weight (non-negative integer)
    
    Returns:
        bool: True if the object will fly, False otherwise
    """
    # Check if the list is balanced (palindromic)
    # Ignore trailing zeros for palindrome check
    trimmed = q
    while trimmed and trimmed[-1] == 0:
        trimmed = trimmed[:-1]
    
    # Check if trimmed list is palindrome
    if trimmed != trimmed[::-1]:
        return False
    
    # Check weight constraint
    if sum(q) > w:
        return False
    
    return True