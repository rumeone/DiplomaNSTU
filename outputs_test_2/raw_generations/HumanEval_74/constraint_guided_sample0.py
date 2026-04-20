"""Module for comparing total character counts in lists of strings."""

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
        The list with the smaller total character count.
        If counts are equal, returns lst1.

    Examples
    --------
    >>> total_match(['hi', 'admin'], ['hI', 'Hi'])
    ['hI', 'Hi']
    >>> total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])
    ['hi', 'admin']
    """
    def total_chars(lst: List[str]) -> int:
        return sum(len(s) for s in lst)

    count1 = total_chars(lst1)
    count2 = total_chars(lst2)

    if count1 <= count2:
        return lst1
    return lst2