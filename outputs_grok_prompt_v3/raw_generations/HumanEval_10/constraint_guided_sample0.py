"""
Utility for constructing shortest palindromic prefixes.
"""

def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with the supplied string.

    The algorithm locates the longest palindromic suffix of the input and
    appends the reverse of the preceding prefix.
    """
    if not string:
        return ""

    for start in range(len(string)):
        suffix = string[start:]
        if suffix == suffix[::-1]:
            prefix = string[:start]
            return string + prefix[::-1]

    # Unreachable: single-character suffix is always a palindrome
    return string