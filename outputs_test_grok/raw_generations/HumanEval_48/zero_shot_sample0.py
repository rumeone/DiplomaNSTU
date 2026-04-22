def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    Examples:
        >>> is_palindrome('racecar')
        True
        >>> is_palindrome('car')
        False
    """
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]