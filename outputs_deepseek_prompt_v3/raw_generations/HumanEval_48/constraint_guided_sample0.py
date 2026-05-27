"""
Palindrome checker module.

This module provides a function to check whether a given string is a palindrome.
"""


def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    A palindrome is a string that reads the same forwards and backwards,
    ignoring case and non-alphanumeric characters.

    Args:
        text: The string to check for palindrome property.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome('racecar')
        True
        >>> is_palindrome('car')
        False
        >>> is_palindrome('A man, a plan, a canal: Panama')
        True
        >>> is_palindrome('No lemon, no melon')
        True
    """
    if not text:
        return True

    cleaned_chars = []
    for char in text:
        if char.isalnum():
            cleaned_chars.append(char.lower())

    cleaned_text = ''.join(cleaned_chars)
    return cleaned_text == cleaned_text[::-1]