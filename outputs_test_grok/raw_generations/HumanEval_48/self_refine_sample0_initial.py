"""Utility functions for string manipulation and checking."""

def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    A palindrome reads the same forwards and backwards, ignoring case,
    spaces, and punctuation.

    Examples:
        >>> is_palindrome('racecar')
        True
        >>> is_palindrome('car')
        False
        >>> is_palindrome('A man, a plan, a canal: Panama')
        True
    """
    if not text:
        return True

    # Create a cleaned version containing only alphanumeric characters
    # and convert to lowercase for case-insensitive comparison
    cleaned = ''.join(char.lower() for char in text if char.isalnum())

    # Compare the string with its reverse using slicing
    return cleaned == cleaned[::-1]