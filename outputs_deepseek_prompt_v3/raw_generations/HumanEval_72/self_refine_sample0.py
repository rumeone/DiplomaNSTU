from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    """
    Determine if an object will fly based on balance and weight constraints.

    The object will fly if it is balanced (palindromic list) and the sum of its
    elements is less than or equal to the maximum possible weight w.

    Args:
        q: A list of non-negative integers representing the object.
        w: A non-negative integer representing the maximum possible weight.

    Returns:
        True if the object will fly, False otherwise.

    Examples:
        >>> will_it_fly([1, 2], 5)
        False
        >>> will_it_fly([3, 2, 3], 9)
        True
        >>> will_it_fly([0, 3], 5)
        True
    """
    # Remove trailing zeros for palindrome check
    trimmed = q[:]
    while trimmed and trimmed[-1] == 0:
        trimmed.pop()

    # Check if trimmed list is palindrome
    if trimmed != trimmed[::-1]:
        return False

    # Check weight constraint
    if sum(q) > w:
        return False

    return True