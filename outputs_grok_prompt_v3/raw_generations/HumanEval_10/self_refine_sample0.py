"""Utility for constructing shortest palindromes."""

def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string.

    The algorithm locates the longest palindromic suffix of the input and
    appends the reverse of the preceding prefix.
    """
    if not string:
        return string

    n = len(string)
    for start in range(n):
        suffix = string[start:]
        if suffix == suffix[::-1]:
            prefix = string[:start]
            return string + prefix[::-1]
    return string  # fallback (unreachable for non-empty input)