from typing import List


def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    len1 = sum(len(s) for s in lst1)
    len2 = sum(len(s) for s in lst2)
    if len1 <= len2:
        return lst1
    return lst2