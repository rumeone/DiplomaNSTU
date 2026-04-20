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
    def total_chars(lst: List[str]) -> int:
        return sum(len(s) for s in lst)

    chars1 = total_chars(lst1)
    chars2 = total_chars(lst2)

    if chars1 <= chars2:
        return lst1
    else:
        return lst2