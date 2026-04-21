"""Module providing the will_it_fly function to determine if an object can fly based on balance and weight constraints."""

from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    """
    Determine if the object q will fly.

    The object will fly if it is balanced (palindromic, ignoring leading/trailing zeros)
    and the sum of its elements is less than or equal to the maximum weight w.

    Args:
        q: List of non-negative integers representing the object.
        w: Non-negative integer representing the maximum possible weight.

    Returns:
        True if the object will fly, False otherwise.

    Examples:
        will_it_fly([1, 2], 5) == False
        will_it_fly([3, 2, 3], 1) == False
        will_it_fly([3, 2, 3], 9) == True
        will_it_fly([0, 3], 5) == True
    """
    if not q:
        return True

    total_weight = sum(q)
    if total_weight > w:
        return False

    # Find the first and last non-zero indices to ignore leading/trailing zeros
    left = 0
    right = len(q) - 1

    while left < right and q[left] == 0:
        left += 1
    while left < right and q[right] == 0:
        right -= 1

    # Check if the trimmed sequence is a palindrome
    while left < right:
        if q[left] != q[right]:
            return False
        left += 1
        right -= 1

    return True