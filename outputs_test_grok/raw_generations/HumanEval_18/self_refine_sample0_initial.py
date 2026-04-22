"""
Module providing utility functions for string analysis.

This module contains functions to analyze occurrences of substrings
within strings, including support for overlapping matches.
"""


def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Example:
        >>> how_many_times('aaaa', 'aa')
        3
    """
    if not substring:
        return 0

    count = 0
    start = 0
    substring_length = len(substring)

    while True:
        position = string.find(substring, start)
        if position == -1:
            break
        count += 1
        start = position + 1

    return count