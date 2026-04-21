"""Module providing a function to compare two lists of strings by total character count."""

from typing import List


def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    """
    Return the list that has fewer total characters across all its strings.

    If both lists have the same total number of characters, return the first list.

    Examples:
        total_match(['hi', 'admin'], ['hI', 'Hi']) -> ['hI', 'Hi']
        total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) -> ['hi', 'admin']
    """
    def total_chars(strings: List[str]) -> int:
        return sum(len(s) for s in strings)

    count1 = total_chars(lst1)
    count2 = total_chars(lst2)

    if count1 <= count2:
        return lst1
    return lst2