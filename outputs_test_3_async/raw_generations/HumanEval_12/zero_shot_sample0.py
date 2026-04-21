from typing import List


def longest(strings: List[str]) -> str:
    """
    Out of a list of strings, return the longest one.
    Return the first one in case of multiple strings of the same length.
    Return an empty string for edge cases.

    Examples:
        >>> longest(['a', 'b', 'c'])
        'a'
        >>> longest(['a', 'bb', 'ccc'])
        'ccc'
    """
    if not strings:
        return ""
    
    longest_str = strings[0]
    for s in strings[1:]:
        if len(s) > len(longest_str):
            longest_str = s
    return longest_str