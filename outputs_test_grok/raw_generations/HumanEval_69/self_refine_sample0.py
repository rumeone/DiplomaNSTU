"""Module providing the search function to find the greatest integer
with frequency greater than or equal to its value.
"""

from typing import List
from collections import Counter


def search(lst: List[int]) -> int:
    """Return the greatest integer > 0 that appears at least as many times
    as its own value. Return -1 if no such integer exists.

    The frequency of an integer is the number of times it appears in the list.

    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    """
    if not lst:
        return -1

    frequency = Counter(lst)
    candidates = []

    for num, count in frequency.items():
        if num > 0 and count >= num:
            candidates.append(num)

    if not candidates:
        return -1

    return max(candidates)