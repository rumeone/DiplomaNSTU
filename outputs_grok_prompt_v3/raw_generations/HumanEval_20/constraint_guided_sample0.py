"""
Module providing a function to find the closest pair of elements in a list.
"""

from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return
    the last two elements that are the closest to each other and return them
    in order (smaller number, larger number).
    """
    min_diff = float("inf")
    best_pair = (0.0, 0.0)
    n = len(numbers)
    for i in range(n - 1):
        for j in range(i + 1, n):
            diff = abs(numbers[j] - numbers[i])
            if diff <= min_diff:
                min_diff = diff
                a, b = numbers[i], numbers[j]
                best_pair = (min(a, b), max(a, b))
    return best_pair