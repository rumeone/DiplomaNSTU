"""Module providing palindrome checking functionality.

This module contains a function to determine whether a given string
is a palindrome, ignoring case, spaces, and punctuation.
"""


def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    A palindrome reads the same forwards and backwards, ignoring
    case, spaces, and punctuation.

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

    # Clean the text: keep only alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in text if char.isalnum())

    # Compare the cleaned string with its reverse
    return cleaned == cleaned[::-1]