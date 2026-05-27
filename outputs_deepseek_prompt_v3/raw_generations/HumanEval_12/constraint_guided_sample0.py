from typing import List


def longest(strings: List[str]) -> str:
    """
    Return the longest string from a list of strings.
    If multiple strings have the same length, return the first one.
    Return an empty string for edge cases (empty list or None).

    Args:
        strings: A list of strings to evaluate.

    Returns:
        The longest string, or an empty string for edge cases.
    """
    if not strings:
        return ''
    
    longest_str = strings[0]
    max_length = len(longest_str)
    
    for s in strings[1:]:
        if len(s) > max_length:
            longest_str = s
            max_length = len(s)
    
    return longest_str