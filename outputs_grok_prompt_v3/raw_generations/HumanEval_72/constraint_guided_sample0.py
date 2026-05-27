"""Utility to determine if an object will fly based on balance and weight."""

from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    """Return True if q is balanced (palindromic after trimming edge zeros)
    and sum(q) <= w; otherwise False.
    """
    total_weight = sum(q)
    if total_weight > w:
        return False

    # Trim leading zeros
    start = 0
    while start < len(q) and q[start] == 0:
        start += 1

    # Trim trailing zeros
    end = len(q)
    while end > start and q[end - 1] == 0:
        end -= 1

    trimmed = q[start:end]
    if trimmed == trimmed[::-1]:
        return True
    return False