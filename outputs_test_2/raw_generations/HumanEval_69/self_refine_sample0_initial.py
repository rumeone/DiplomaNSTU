from typing import List


def search(lst: List[int]) -> int:
    """
    Return the greatest integer that is greater than zero and has a frequency
    greater than or equal to the integer's value. If no such value exists,
    return -1.

    Args:
        lst: A non-empty list of positive integers.

    Returns:
        The greatest integer meeting the frequency condition, or -1 if none exist.
    """
    frequency = {}
    for num in lst:
        frequency[num] = frequency.get(num, 0) + 1

    valid_numbers = []
    for num, count in frequency.items():
        if num > 0 and count >= num:
            valid_numbers.append(num)

    if not valid_numbers:
        return -1

    return max(valid_numbers)