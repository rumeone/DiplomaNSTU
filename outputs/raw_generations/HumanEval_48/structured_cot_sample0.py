def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    Examples:
        >>> is_palindrome('racecar')
        True
        >>> is_palindrome('car')
        False
    """
    left = 0
    right = len(text) - 1
    
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    
    return True