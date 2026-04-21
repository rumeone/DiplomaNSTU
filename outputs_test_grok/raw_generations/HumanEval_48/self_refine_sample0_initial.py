"""Module providing palindrome checking functionality.

This module contains a function to determine whether a given string
is a palindrome, ignoring case, spaces, and punctuation.
"""


def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    A palindrome is a string that reads the same forwards and backwards,
    ignoring case, spaces, and punctuation.

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

    # Clean the string: keep only alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in text if char.isalnum())

    # Compare string with its reverse using two pointers (early return on mismatch)
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True