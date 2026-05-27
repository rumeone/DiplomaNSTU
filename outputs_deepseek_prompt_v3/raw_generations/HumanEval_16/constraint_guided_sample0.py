"""
Module for counting distinct characters in a string, ignoring case differences.
"""


def count_distinct_characters(string: str) -> int:
    """
    Find out how many distinct characters (regardless of case) are in the string.

    Args:
        string: The input string to analyze.

    Returns:
        The number of distinct characters, ignoring case.

    Examples:
        >>> count_distinct_characters("xyzXYZ")
        3
        >>> count_distinct_characters("Jerry")
        4
    """
    if not string:
        return 0

    distinct_chars = set(char.lower() for char in string)
    return len(distinct_chars)