"""
Module for checking if a string is a palindrome.
"""


def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    A palindrome is a string that reads the same forwards and backwards,
    ignoring case and non-alphanumeric characters.

    Args:
        text: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome('racecar')
        True
        >>> is_palindrome('car')
        False
        >>> is_palindrome('A man, a plan, a canal: Panama')
        True
        >>> is_palindrome('')
        True
        >>> is_palindrome('a')
        True
    """
    if not text:
        return True

    cleaned_chars = []
    for char in text.lower():
        if char.isalnum():
            cleaned_chars.append(char)

    cleaned_text = ''.join(cleaned_chars)
    left = 0
    right = len(cleaned_text) - 1

    while left < right:
        if cleaned_text[left] != cleaned_text[right]:
            return False
        left += 1
        right -= 1

    return True