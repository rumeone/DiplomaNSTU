from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    """
    Determine if object q will fly based on balance and weight constraints.

    The object flies if:
    1. It is balanced (palindromic list)
    2. The sum of its elements ≤ maximum weight w

    Args:
        q: List of non-negative integers representing connected object
        w: Non-negative integer representing maximum possible weight

    Returns:
        bool: True if object will fly, False otherwise
    """
    # Check if list is palindromic
    is_balanced = q == q[::-1]
    
    # Check weight constraint
    weight_ok = sum(q) <= w
    
    return is_balanced and weight_ok