"""
This module provides a function to find the longest string in a list.
"""

from typing import List


def longest(strings: List[str]) -> str:
    """
    Return the longest string from a list of strings.
    
    If multiple strings have the same maximum length, return the first one.
    If the input list is empty or None, return an empty string.
    
    Args:
        strings: A list of strings to search through.
    
    Returns:
        The longest string, or an empty string for edge cases.
    
    Examples:
        >>> longest(['a', 'b', 'c'])
        'a'
        >>> longest(['a', 'bb', 'ccc'])
        'ccc'
        >>> longest([])
        ''
        >>> longest(['hello', 'world', 'test'])
        'hello'
    """
    if not strings:
        return ''
    
    longest_str = strings[0]
    
    for s in strings[1:]:
        if len(s) > len(longest_str):
            longest_str = s
    
    return longest_str