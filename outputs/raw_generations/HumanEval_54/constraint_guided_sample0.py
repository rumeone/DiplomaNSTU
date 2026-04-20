def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # Compare sorted character lists
    return sorted(s0) == sorted(s1)