def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    Examples:
        >>> is_palindrome('racecar')
        True
        >>> is_palindrome('car')
        False
    """
    cleaned = text.lower()
    return cleaned == cleaned[::-1]