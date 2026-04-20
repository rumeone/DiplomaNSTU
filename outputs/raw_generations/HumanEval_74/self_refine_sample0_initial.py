from typing import List


def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    total_chars_lst1 = sum(len(s) for s in lst1)
    total_chars_lst2 = sum(len(s) for s in lst2)

    if total_chars_lst1 <= total_chars_lst2:
        return lst1
    else:
        return lst2