from typing import List


def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    """
    Return the list with fewer total characters across all strings.
    If equal, return the first list.
    """
    if not isinstance(lst1, list) or not isinstance(lst2, list):
        raise TypeError("Both arguments must be lists")

    total1 = sum(len(s) for s in lst1 if isinstance(s, str))
    total2 = sum(len(s) for s in lst2 if isinstance(s, str))

    return lst1 if total1 <= total2 else lst2