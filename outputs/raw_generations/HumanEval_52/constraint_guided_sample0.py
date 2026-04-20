from typing import List


def below_threshold(l: List[int], t: int) -> bool:
    """
    Check if all numbers in the list l are below threshold t.
    """
    for num in l:
        if num >= t:
            return False
    return True