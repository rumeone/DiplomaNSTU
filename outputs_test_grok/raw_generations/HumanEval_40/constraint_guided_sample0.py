"""Module providing a function to check if three distinct elements in a list sum to zero."""

from typing import List


def triples_sum_to_zero(l: List[int]) -> bool:
    """
    Check if there are three distinct elements in the list that sum to zero.

    Examples:
        >>> triples_sum_to_zero([1, 3, 5, 0])
        False
        >>> triples_sum_to_zero([1, 3, -2, 1])
        True
    """
    if len(l) < 3:
        return False

    # Sort a copy to enable two-pointer technique while preserving original order
    nums = sorted(l)

    for i in range(len(nums) - 2):
        # Skip duplicate values for the first element to avoid redundant checks
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1
        target = -nums[i]

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return True
            if current_sum < target:
                left += 1
            else:
                right -= 1

    return False