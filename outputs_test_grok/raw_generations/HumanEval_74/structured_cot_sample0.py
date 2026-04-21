from typing import List


def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    """
    Write a function that accepts two lists of strings and returns the list that has 
    less total number of chars in the all strings of the list compared to the other list.

    If the two lists have the same number of chars, return the first list.

    Examples:
        total_match(['hi', 'admin'], ['hI', 'Hi']) -> ['hI', 'Hi']
        total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) -> ['hi', 'admin']
    """
    len1 = sum(len(s) for s in lst1)
    len2 = sum(len(s) for s in lst2)
    return lst1 if len1 <= len2 else lst2