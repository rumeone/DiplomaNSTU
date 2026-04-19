from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    if not q:
        return False

    if sum(q) > w:
        return False

    left = 0
    right = len(q) - 1
    while left < right:
        if q[left] != q[right]:
            return False
        left += 1
        right -= 1

    return True