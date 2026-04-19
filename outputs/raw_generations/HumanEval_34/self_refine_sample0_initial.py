def unique(l: List[int]) -> List[int]:
    """
    Return sorted unique elements in a list.
    """
    # Convert to set to remove duplicates, then sort
    return sorted(set(l))