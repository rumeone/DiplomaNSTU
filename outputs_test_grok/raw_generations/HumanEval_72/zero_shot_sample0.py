from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    if sum(q) > w:
        return False
    n = len(q)
    i = 0
    j = n - 1
    while i < j:
        if q[i] == 0:
            i += 1
            continue
        if q[j] == 0:
            j -= 1
            continue
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1
    return True