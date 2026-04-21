"""
This module provides a function to compare two lists of strings based on the
total number of characters in all strings within each list.
"""

from typing import List


def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    """
    Return the list with fewer total characters across all its strings.

    Parameters
    ----------
    lst1 : List[str]
        First list of strings.
    lst2 : List[str]
        Second list of strings.

    Returns
    -------
    List[str]
        The list with fewer total characters. If both lists have the same
        total characters, returns the first list.

    Examples
    --------
    >>> total_match(['hi', 'admin'], ['hI', 'Hi'])
    ['hI', 'Hi']
    >>> total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])
    ['hi', 'admin']
    """
    total_chars_lst1 = sum(len(s) for s in lst1)
    total_chars_lst2 = sum(len(s) for s in lst2)

    if total_chars_lst2 < total_chars_lst1:
        return lst2
    return lst1