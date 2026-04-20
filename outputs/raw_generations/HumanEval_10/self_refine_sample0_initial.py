def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    """
    if not string:
        return ""

    def is_palindrome(s):
        return s == s[::-1]

    # Find the longest palindromic suffix
    for i in range(len(string)):
        suffix = string[i:]
        if is_palindrome(suffix):
            # Prefix that needs to be appended in reverse
            prefix = string[:i]
            return string + prefix[::-1]

    # Fallback: entire string is not a palindrome, append all but last character reversed
    return string + string[:-1][::-1]