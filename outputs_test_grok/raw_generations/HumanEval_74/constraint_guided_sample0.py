"""Module providing a function to compare two lists of strings by total character count."""

from typing import List


def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    """
    Return the list that has less total number of chars in all its strings.

    If the two lists have the same number of chars, return the first list.

    Examples:
        total_match(['hi', 'admin'], ['hI', 'Hi']) -> ['hI', 'Hi']
        total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) -> ['hi', 'admin']
    """
    def total_chars(strings: List[str]) -> int:
        return sum(len(s) for s in strings)

    count1 = total_chars(lst1)
    count2 = total_chars(lst2)

    if count2 < count1:
        return lst2

    return lst1