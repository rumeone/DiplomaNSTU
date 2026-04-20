def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.
    """
    if not isinstance(text, str):
        return False
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True