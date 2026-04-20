from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    # Check if the list is palindromic
    is_palindrome = True
    left, right = 0, len(q) - 1
    while left < right:
        if q[left] != q[right]:
            is_palindrome = False
            break
        left += 1
        right -= 1

    # Check if sum is within weight limit
    total_weight = sum(q)
    weight_ok = total_weight <= w

    return is_palindrome and weight_ok