from typing import List


def longest(strings: List[str]) -> str:
    """
    Return the longest string from a list of strings.

    If multiple strings have the same maximum length, return the first one.
    For empty lists or None input, return an empty string.

    Args:
        strings: A list of strings to search through.

    Returns:
        The longest string, or empty string for edge cases.

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
        return ""

    longest_str = strings[0]
    max_length = len(longest_str)

    for string in strings[1:]:
        current_length = len(string)
        if current_length > max_length:
            longest_str = string
            max_length = current_length

    return longest_str