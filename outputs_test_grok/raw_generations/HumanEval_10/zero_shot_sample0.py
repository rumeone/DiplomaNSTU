def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

    Examples:
        >>> make_palindrome("cat")
        "catac"
        >>> make_palindrome("cata")
        "catac"
    """
    n = len(string)
    if n == 0:
        return ""
    
    # Find the longest suffix that is a palindrome
    for i in range(n - 1, -1, -1):
        suffix = string[i:]
        if suffix == suffix[::-1]:
            # The prefix before this suffix needs to be reversed and appended
            prefix = string[:i]
            return string + prefix[::-1]
    
    # This should never be reached for non-empty strings
    return string