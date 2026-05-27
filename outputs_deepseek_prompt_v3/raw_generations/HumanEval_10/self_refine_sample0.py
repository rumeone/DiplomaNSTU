"""
Module for creating palindromes from strings.
"""


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.

    Algorithm:
    1. Find the longest suffix of the string that is a palindrome.
    2. Append the reverse of the prefix (before that palindrome suffix)
       to the end of the string.

    Args:
        string: The input string to extend into a palindrome.

    Returns:
        The shortest palindrome that starts with the input string.

    Examples:
        >>> make_palindrome("cat")
        'catac'
        >>> make_palindrome("cata")
        'catac'
    """
    if not string:
        return ""

    length = len(string)

    # Find the longest palindromic suffix
    for i in range(length):
        suffix = string[i:]
        if suffix == suffix[::-1]:
            # Found the longest palindromic suffix
            prefix_to_add = string[:i][::-1]
            return string + prefix_to_add

    # Fallback: entire string is not a palindrome, reverse and append all but last char
    return string + string[:-1][::-1]