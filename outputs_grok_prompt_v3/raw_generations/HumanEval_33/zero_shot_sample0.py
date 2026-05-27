from typing import List

def sort_third(l: List[int]) -> List[int]:
    sorted_thirds = sorted(l[i] for i in range(0, len(l), 3))
    result = l[:]
    for i, val in enumerate(sorted_thirds):
        result[i * 3] = val
    return result