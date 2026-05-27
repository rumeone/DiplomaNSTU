"""Utility for detecting zero-sum triples in integer lists."""

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
    if len(l) < 3:
        return False

    nums = sorted(l)
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                return True
            if current_sum < 0:
                left += 1
            else:
                right -= 1
    return False