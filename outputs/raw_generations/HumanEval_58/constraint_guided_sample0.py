from typing import List


def common(l1: List[int], l2: List[int]) -> List[int]:
    """
    Return sorted unique common elements for two integer lists.
    """
    # Convert lists to sets for efficient intersection and uniqueness
    set1 = set(l1)
    set2 = set(l2)
    
    # Find common elements
    common_elements = set1.intersection(set2)
    
    # Return sorted list
    return sorted(common_elements)