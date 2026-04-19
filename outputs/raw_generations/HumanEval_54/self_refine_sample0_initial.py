def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # Compare sorted characters after removing duplicates
    return sorted(set(s0)) == sorted(set(s1))