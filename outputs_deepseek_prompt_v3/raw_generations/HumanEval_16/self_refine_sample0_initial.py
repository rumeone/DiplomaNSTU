"""
This module provides a function to count distinct characters in a string,
ignoring case differences.
"""


def count_distinct_characters(string: str) -> int:
    """
    Return the number of distinct characters in the given string,
    treating uppercase and lowercase letters as the same.

    Parameters
    ----------
    string : str
        The input string to analyze.

    Returns
    -------
    int
        The count of distinct characters (case-insensitive).

    Examples
    --------
    >>> count_distinct_characters("xyzXYZ")
    3
    >>> count_distinct_characters("Jerry")
    4
    """
    if not string:
        return 0

    return len({char.lower() for char in string})