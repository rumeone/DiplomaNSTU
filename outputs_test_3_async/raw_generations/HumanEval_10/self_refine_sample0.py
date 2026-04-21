"""
Shortest palindrome construction from a given string.
"""


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with the supplied string.

    Algorithm:
    1. Find the longest suffix of the string that is a palindrome.
    2. Append the reverse of the prefix (before that palindrome suffix)
       to the end of the original string.

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
            # Prefix that needs to be mirrored
            prefix = string[:i]
            return string + prefix[::-1]

    # Fallback: entire string is not a palindrome, mirror everything except last char
    return string + string[-2::-1]