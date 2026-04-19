def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    """
    if not string:
        return ""

    # Find the longest palindromic suffix
    for i in range(len(string)):
        suffix = string[i:]
        if suffix == suffix[::-1]:
            prefix = string[:i]
            return string + prefix[::-1]

    # This line should never be reached, but kept for safety
    return string + string[::-1]