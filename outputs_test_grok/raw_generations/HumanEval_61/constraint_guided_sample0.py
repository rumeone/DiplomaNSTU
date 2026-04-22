"""
Module providing a function to check if brackets in a string are correctly matched.
"""


def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket has a corresponding closing bracket.

    The function verifies that brackets are properly nested and matched.
    It returns True only if all opening brackets have corresponding closing
    brackets in the correct order.

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
    if not brackets:
        return True

    open_count = 0
    for char in brackets:
        if char == "(":
            open_count += 1
        elif char == ")":
            open_count -= 1
            if open_count < 0:
                return False

    return open_count == 0