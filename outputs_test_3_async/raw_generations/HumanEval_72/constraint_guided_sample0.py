from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    """
    Determine if an object will fly based on balance and weight constraints.

    The object will fly if:
    1. It is balanced (palindromic list when ignoring leading/trailing zeros)
    2. The sum of its elements is less than or equal to the maximum weight w

    Args:
        q: List of non-negative integers representing the object's structure
        w: Non-negative integer representing maximum allowed weight

    Returns:
        bool: True if the object will fly, False otherwise
    """
    # Check weight constraint
    if sum(q) > w:
        return False

    # Check balance (palindromic) constraint
    # Remove leading and trailing zeros as they don't affect balance
    trimmed = q[:]
    while trimmed and trimmed[0] == 0:
        trimmed.pop(0)
    while trimmed and trimmed[-1] == 0:
        trimmed.pop()

    # Check if trimmed list is palindromic
    return trimmed == trimmed[::-1]