from typing import List


def below_threshold(l: List[int], t: int) -> bool:
    """
    Check if all numbers in the list l are below threshold t.

    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    if not l:
        return True
    return all(num < t for num in l)