from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    """
    Determine if an object will fly based on balance and weight constraints.

    The object will fly if:
    1. It is balanced (palindromic list).
    2. The sum of its elements is <= maximum weight w.

    Parameters:
    q: List of non-negative integers representing the object.
    w: Non-negative integer representing maximum weight.

    Returns:
    bool: True if the object will fly, False otherwise.
    """
    # Check if the list is palindromic
    if q != q[::-1]:
        return False

    # Check weight constraint
    if sum(q) > w:
        return False

    return True