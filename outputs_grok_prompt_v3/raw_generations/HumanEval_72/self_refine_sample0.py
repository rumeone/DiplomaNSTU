"""Utility to determine if a given object will fly based on balance and weight."""

from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    """
    Return True if q is balanced (its non-zero core is palindromic)
    and sum(q) <= w; otherwise False.
    """
    if w < 0:
        return False
    # Strip leading/trailing zeros to obtain the connected core
    start = 0
    while start < len(q) and q[start] == 0:
        start += 1
    end = len(q) - 1
    while end >= start and q[end] == 0:
        end -= 1
    if start > end:
        return True  # all zeros, sum is 0
    core = q[start : end + 1]
    if core != core[::-1]:
        return False
    return sum(q) <= w