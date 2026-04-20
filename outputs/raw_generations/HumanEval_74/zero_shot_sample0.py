from typing import List

def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    total1 = sum(len(s) for s in lst1)
    total2 = sum(len(s) for s in lst2)
    if total1 <= total2:
        return lst1
    else:
        return lst2