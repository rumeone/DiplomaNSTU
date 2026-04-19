from typing import List


def sort_even(l: List[int]) -> List[int]:
    even_values = [l[i] for i in range(0, len(l), 2)]
    even_values.sort()
    result = l[:]
    for i in range(0, len(l), 2):
        result[i] = even_values[i // 2]
    return result