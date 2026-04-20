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
    max_length = len(longest_str)
    
    for s in strings[1:]:
        if len(s) > max_length:
            longest_str = s
            max_length = len(s)
    
    return longest_str