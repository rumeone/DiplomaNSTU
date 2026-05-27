from typing import List


def search(lst: List[int]) -> int:
    """
    Return the greatest integer that is greater than zero and has a frequency
    greater than or equal to the integer itself. If no such value exists,
    return -1.

    Args:
        lst: A non-empty list of positive integers.

    Returns:
        The greatest integer meeting the criteria, or -1 if none exists.
    """
    frequency = {}
    for num in lst:
        frequency[num] = frequency.get(num, 0) + 1

    candidates = []
    for num, count in frequency.items():
        if num > 0 and count >= num:
            candidates.append(num)

    if not candidates:
        return -1

    return max(candidates)