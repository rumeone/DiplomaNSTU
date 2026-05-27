def common(l1: List[int], l2: List[int]) -> List[int]:
    return sorted(set(l1) & set(l2))