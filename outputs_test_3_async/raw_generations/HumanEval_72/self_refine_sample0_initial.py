from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    """
    Determine if an object will fly based on balance and weight constraints.

    The object will fly if:
    1. It is balanced (palindromic list, ignoring zeros for balance)
    2. The sum of its elements is <= maximum weight w

    Args:
        q: List of non-negative integers representing the object.
        w: Non-negative integer representing maximum allowed weight.

    Returns:
        True if the object will fly, False otherwise.
    """
    # Check weight constraint
    if sum(q) > w:
        return False

    # Check balance (palindrome)
    # Filter out zeros for balance check as per examples
    non_zero = [x for x in q if x != 0]
    return non_zero == non_zero[::-1]