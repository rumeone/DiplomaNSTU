"""
Module providing a function to generate all prefixes of a given string.
"""

from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    if not string:
        return []

    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])

    return prefixes