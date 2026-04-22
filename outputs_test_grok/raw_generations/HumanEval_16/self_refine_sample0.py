"""
Module providing functions to analyze distinct characters in strings.
"""


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

    # Convert to lowercase and use a set to track unique characters
    unique_chars = set(string.lower())
    return len(unique_chars)