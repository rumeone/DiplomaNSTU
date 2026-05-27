from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    """
    Determine if an object will fly based on balance and weight constraints.

    The object flies if:
    1. It is balanced (palindromic list when ignoring zeros between non-zero elements).
    2. The sum of its elements is less than or equal to the maximum weight w.

    Parameters:
    q: List of non-negative integers representing the object's parts.
    w: Non-negative integer representing the maximum allowable weight.

    Returns:
    bool: True if the object will fly, False otherwise.
    """
    # Check if the list is balanced (palindromic ignoring zeros between non-zero)
    # First, filter out zeros that are between non-zero elements
    filtered_q = []
    non_zero_seen = False
    for num in q:
        if num != 0:
            non_zero_seen = True
            filtered_q.append(num)
        elif not non_zero_seen:
            # Leading zeros are included for balance check
            filtered_q.append(num)

    # Check if filtered list is palindromic
    if filtered_q != filtered_q[::-1]:
        return False

    # Check weight constraint
    if sum(q) > w:
        return False

    return True