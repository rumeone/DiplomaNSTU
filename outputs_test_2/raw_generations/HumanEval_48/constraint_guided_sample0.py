"""
Module for checking if a string is a palindrome.
"""


def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    A palindrome is a string that reads the same forwards and backwards,
    ignoring case and non-alphanumeric characters.

    Examples:
        >>> is_palindrome('racecar')
        True
        >>> is_palindrome('car')
        False
    """
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]