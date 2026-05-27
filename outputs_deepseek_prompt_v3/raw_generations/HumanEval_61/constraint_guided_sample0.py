"""
Module for checking if brackets in a string are correctly matched.
"""


def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket has a corresponding closing bracket.

    The function iterates through the string, maintaining a count of unmatched
    opening brackets. If at any point the count becomes negative (more closing
    than opening brackets), the string is invalid. At the end, the count must
    be zero for the string to be valid.

    Args:
        brackets: A string containing only '(' and ')' characters.

    Returns:
        True if brackets are correctly matched, False otherwise.

    Examples:
        >>> correct_bracketing("(")
        False
        >>> correct_bracketing("()")
        True
        >>> correct_bracketing("(()())")
        True
        >>> correct_bracketing(")(()")
        False
    """
    open_count = 0

    for char in brackets:
        if char == '(':
            open_count += 1
        elif char == ')':
            open_count -= 1
            if open_count < 0:
                return False

    return open_count == 0