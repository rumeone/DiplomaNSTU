def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.
    
    Examples:
        >>> is_palindrome('racecar')
        True
        >>> is_palindrome('car')
        False
    """
    # Compare the string with its reverse
    return text == text[::-1]