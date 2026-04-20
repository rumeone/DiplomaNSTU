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
    
    # Find the longest palindromic suffix
    for i in range(n):
        # Check if substring from i to end is palindrome
        if string[i:] == string[i:][::-1]:
            # Prefix that needs to be appended in reverse
            prefix = string[:i]
            return string + prefix[::-1]
    
    # Fallback (should never reach here for valid strings)
    return string + string[::-1]