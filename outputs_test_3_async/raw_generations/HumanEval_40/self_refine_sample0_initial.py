"""
Module for checking if a list contains three distinct elements that sum to zero.
"""

from typing import List


def triples_sum_to_zero(l: List[int]) -> bool:
    """
    Check if there are three distinct elements in the list that sum to zero.

    Args:
        l: List of integers to check.

    Returns:
        True if there exist three distinct indices i, j, k such that
        l[i] + l[j] + l[k] == 0, False otherwise.

    Examples:
        >>> triples_sum_to_zero([1, 3, 5, 0])
        False
        >>> triples_sum_to_zero([1, 3, -2, 1])
        True
    """
    n = len(l)
    if n < 3:
        return False

    # Sort the list to use two-pointer technique
    sorted_list = sorted(l)

    for i in range(n - 2):
        # Skip duplicate values for the first element
        if i > 0 and sorted_list[i] == sorted_list[i - 1]:
            continue

        left = i + 1
        right = n - 1
        target = -sorted_list[i]

        while left < right:
            current_sum = sorted_list[left] + sorted_list[right]

            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
                # Skip duplicates for left pointer
                while left < right and sorted_list[left] == sorted_list[left - 1]:
                    left += 1
            else:
                right -= 1
                # Skip duplicates for right pointer
                while left < right and sorted_list[right] == sorted_list[right + 1]:
                    right -= 1

    return False