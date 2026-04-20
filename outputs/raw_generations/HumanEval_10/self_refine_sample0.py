def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    """
    if not string:
        return ""

    def is_palindrome(s):
        return s == s[::-1]

    for i in range(len(string)):
        suffix = string[i:]
        if is_palindrome(suffix):
            prefix = string[:i]
            return string + prefix[::-1]

    return string + string[:-1][::-1]