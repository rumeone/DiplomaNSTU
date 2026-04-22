from typing import List


def triples_sum_to_zero(l: List[int]) -> bool:
    """
    Check if there are three distinct elements
    in the list that sum to zero.

    Examples:
        >>> triples_sum_to_zero([1, 3, 5, 0])
        False
        >>> triples_sum_to_zero([1, 3, -2, 1])
        True
    """
    seen = set()
    for i, a in enumerate(l):
        if a in seen:
            continue
        seen.add(a)
        target_set = set()
        for b in l[i + 1 :]:
            if -a - b in target_set:
                return True
            target_set.add(b)
    return False