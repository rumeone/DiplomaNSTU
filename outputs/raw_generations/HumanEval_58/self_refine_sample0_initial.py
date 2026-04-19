from typing import List


def common(l1: List[int], l2: List[int]) -> List[int]:
    """
    Return sorted unique common elements for two integer lists.
    """
    set1 = set(l1)
    set2 = set(l2)
    common_elements = set1.intersection(set2)
    return sorted(common_elements)