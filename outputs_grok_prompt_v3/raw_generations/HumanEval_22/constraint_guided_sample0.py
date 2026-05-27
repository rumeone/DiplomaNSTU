"""
Module providing integer filtering utilities for string lists.
"""
from typing import List


def filter_integers(values: List[str]) -> List[int]:
    """
    Filter given list of string values only for integers.

    Example:
        >>> filter_integers(['10', ' 123 ', '5.0', 'three', 'abc', '{}'])
        [10]
    """
    integer_values: List[int] = []
    for value in values:
        if value.strip().isdigit():
            integer_values.append(int(value))
    return integer_values