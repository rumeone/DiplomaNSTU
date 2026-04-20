"""
Module for creating palindromes from strings.
"""


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.

    Algorithm:
    1. Find the longest suffix of the supplied string that is a palindrome.
    2. Append to the end of the string the reverse of the prefix that comes
       before the palindromic suffix.

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

    # Find the longest palindromic suffix
    for i in range(len(string)):
        suffix = string[i:]
        if suffix == suffix[::-1]:
            # Found the longest palindromic suffix
            prefix = string[:i]
            return string + prefix[::-1]

    # Fallback: entire string is not a palindrome, reverse the whole thing
    return string + string[::-1]