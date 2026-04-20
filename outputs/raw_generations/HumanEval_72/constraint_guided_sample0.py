from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    # Check if the list is palindromic
    is_palindromic = q == q[::-1]
    # Check if the sum of elements is less than or equal to w
    sum_leq_weight = sum(q) <= w
    # The object flies only if both conditions are satisfied
    return is_palindromic and sum_leq_weight