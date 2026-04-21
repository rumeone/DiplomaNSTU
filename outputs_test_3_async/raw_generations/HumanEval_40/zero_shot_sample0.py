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
    n = len(l)
    if n < 3:
        return False
    l_sorted = sorted(l)
    for i in range(n - 2):
        if i > 0 and l_sorted[i] == l_sorted[i - 1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = l_sorted[i] + l_sorted[left] + l_sorted[right]
            if current_sum == 0:
                return True
            elif current_sum < 0:
                left += 1
                while left < right and l_sorted[left] == l_sorted[left - 1]:
                    left += 1
            else:
                right -= 1
                while left < right and l_sorted[right] == l_sorted[right + 1]:
                    right -= 1
    return False