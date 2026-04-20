from typing import List


def triples_sum_to_zero(l: List[int]) -> bool:
    """
    Check if there are three distinct elements
    in the list that sum to zero.
    """
    n = len(l)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False