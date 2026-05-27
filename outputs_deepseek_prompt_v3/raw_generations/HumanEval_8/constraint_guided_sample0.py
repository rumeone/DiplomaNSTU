"""
Module for calculating sum and product of a list of integers.
"""

from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all integers in a list.

    Args:
        numbers: A list of integers to process.

    Returns:
        A tuple containing (sum, product) of all integers in the list.
        For an empty list, returns (0, 1).

    Examples:
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
        >>> sum_product([])
        (0, 1)
        >>> sum_product([5])
        (5, 5)
    """
    if not numbers:
        return (0, 1)

    total_sum = 0
    total_product = 1

    for number in numbers:
        total_sum += number
        total_product *= number

    return (total_sum, total_product)