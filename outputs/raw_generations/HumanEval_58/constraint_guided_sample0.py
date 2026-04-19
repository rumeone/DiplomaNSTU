from typing import List


def common(l1: List[int], l2: List[int]) -> List[int]:
    """
    Return sorted unique common elements for two integer lists.

    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    # Convert lists to sets for O(1) lookups and intersection
    set1 = set(l1)
    set2 = set(l2)
    
    # Find intersection of the two sets
    common_elements = set1.intersection(set2)
    
    # Return sorted list of unique common elements
    return sorted(common_elements)