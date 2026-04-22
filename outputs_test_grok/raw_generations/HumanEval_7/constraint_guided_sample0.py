"""Filter lists of strings based on substring presence."""

from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Example:
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    if not substring:
        return strings[:]

    return [s for s in strings if substring in s]