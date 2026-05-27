from typing import List

def pairs_sum_to_zero(l: List[int]) -> bool:
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False