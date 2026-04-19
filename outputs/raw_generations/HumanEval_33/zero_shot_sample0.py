from typing import List


def sort_third(l: List[int]) -> List[int]:
    result = []
    divisible_by_three = []
    for i, val in enumerate(l):
        if i % 3 == 0:
            divisible_by_three.append(val)
        else:
            result.append(val)
    divisible_by_three.sort()
    for i, val in enumerate(l):
        if i % 3 == 0:
            result.insert(i, divisible_by_three[i // 3])
    return result