"""Utility for counting distinct characters in strings."""

def count_distinct_characters(string: str) -> int:
    """Find out how many distinct characters (regardless of case) are in the string.

    Examples:
        >>> count_distinct_characters("xyzXYZ")
        3
        >>> count_distinct_characters("Jerry")
        4
    """
    if not string:
        return 0
    lowercase = string.lower()
    distinct_characters = set(lowercase)
    return len(distinct_characters)