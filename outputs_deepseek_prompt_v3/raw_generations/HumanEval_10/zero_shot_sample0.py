def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    n = len(string)
    if n == 0:
        return ""
    
    # Find the longest palindromic suffix
    for i in range(n):
        # Check if substring from i to end is palindrome
        suffix = string[i:]
        if suffix == suffix[::-1]:
            # Prefix before the palindromic suffix
            prefix = string[:i]
            # Append reverse of prefix to original string
            return string + prefix[::-1]
    
    # Fallback: if no palindromic suffix found (should not happen for i=0)
    return string + string[::-1]