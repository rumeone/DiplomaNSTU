"""Utility module for computing aggregate values over lists of integers."""

from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Example:
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    if not numbers:
        return 0, 1

    total_sum = 0
    product = 1
    for value in numbers:
        total_sum += value
        product *= value
    return total_sum, product