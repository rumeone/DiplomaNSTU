"""
Module for creating palindromes from strings.
"""


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.

    Algorithm:
    1. Find the longest suffix of the string that is a palindrome.
    2. Append the reverse of the prefix (before the palindromic suffix)
       to the end of the string.

    Examples:
        >>> make_palindrome("cat")
        'catac'
        >>> make_palindrome("cata")
        'catac'
    """
    if not string:
        return ""

    def is_palindrome(s: str) -> bool:
        """Check if a string is a palindrome."""
        return s == s[::-1]

    # Find the longest palindromic suffix
    for i in range(len(string)):
        suffix = string[i:]
        if is_palindrome(suffix):
            # Prefix is the part before the palindromic suffix
            prefix = string[:i]
            return string + prefix[::-1]

    # Fallback: entire string is not a palindrome, reverse whole string
    return string + string[::-1]