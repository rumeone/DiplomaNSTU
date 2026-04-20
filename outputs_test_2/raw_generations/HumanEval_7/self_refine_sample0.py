from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter strings that contain the given substring.

    Args:
        strings: A list of strings to filter.
        substring: The substring to search for.

    Returns:
        A list containing only the strings from the input list
        that contain the specified substring.

    Example:
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    if not strings:
        return []

    if not substring:
        return strings[:]

    return [s for s in strings if substring in s]