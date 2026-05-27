"""Module providing the search function for frequency-based integer lookup."""

from typing import List
from collections import Counter


def search(lst: List[int]) -> int:
    """
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than
    zero, and has a frequency greater than or equal to the value of the integer itself.
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    """
    frequency = Counter(lst)
    result = -1
    for number, count in frequency.items():
        if number > 0 and count >= number and number > result:
            result = number
    return result