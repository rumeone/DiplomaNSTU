"""
Module for counting distinct characters in a string, case-insensitively.
"""


def count_distinct_characters(string: str) -> int:
    """
    Return the number of distinct characters in the string, ignoring case.

    Parameters
    ----------
    string : str
        The input string to analyze.

    Returns
    -------
    int
        The number of distinct characters (case-insensitive).

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