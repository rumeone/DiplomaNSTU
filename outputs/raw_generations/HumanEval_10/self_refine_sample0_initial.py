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
            # Append reverse of prefix before this suffix
            prefix = string[:i]
            return string + prefix[::-1]

    # Fallback: entire string is not a palindrome, reverse whole string
    return string + string[:-1][::-1]