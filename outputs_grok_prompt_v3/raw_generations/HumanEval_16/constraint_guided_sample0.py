"""Utility for counting distinct characters case-insensitively."""

def count_distinct_characters(string: str) -> int:
    """
    Find out how many distinct characters (regardless of case) are in the string.

    Examples:
        >>> count_distinct_characters("xyzXYZ")
        3
        >>> count_distinct_characters("Jerry")
        4
    """
    if not string:
        return 0
    lowered = string.lower()
    distinct_chars = set(lowered)
    return len(distinct_chars)