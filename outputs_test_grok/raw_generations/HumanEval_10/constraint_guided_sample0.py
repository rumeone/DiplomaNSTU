"""
Module providing functionality to create the shortest palindrome
that begins with a given string.
"""


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.

    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that
      comes before the palindromic suffix.

    Examples:
        >>> make_palindrome("cat")
        'catac'
        >>> make_palindrome("cata")
        'catac'
    """
    if not string:
        return ""

    n = len(string)
    # Check for longest palindromic suffix
    for i in range(n):
        suffix = string[i:]
        if suffix == suffix[::-1]:
            # Found the longest palindromic suffix starting at i
            prefix_to_reverse = string[:i]
            return string + prefix_to_reverse[::-1]

    # This should never be reached for non-empty strings
    return string