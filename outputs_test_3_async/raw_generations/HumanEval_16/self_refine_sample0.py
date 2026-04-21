def count_distinct_characters(string: str) -> int:
    """
    Return the number of distinct characters in the given string.

    The comparison is case-insensitive, meaning 'a' and 'A' are considered
    the same character.

    Args:
        string: The input string to analyze.

    Returns:
        The number of distinct characters (case-insensitive).

    Examples:
        >>> count_distinct_characters("xyzXYZ")
        3
        >>> count_distinct_characters("Jerry")
        4
    """
    return len({char.lower() for char in string})