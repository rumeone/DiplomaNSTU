"""
Module for checking bracket balancing in strings containing '<' and '>'.
"""


def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket '<' has a corresponding closing bracket '>'.

    Args:
        brackets: A string containing only '<' and '>' characters.

    Returns:
        True if every opening bracket is properly matched with a closing bracket,
        False otherwise.

    Examples:
        >>> correct_bracketing("<")
        False
        >>> correct_bracketing("<>")
        True
        >>> correct_bracketing("<<><>>")
        True
        >>> correct_bracketing("><<>")
        False
    """
    balance = 0

    for char in brackets:
        if char == "<":
            balance += 1
        elif char == ">":
            balance -= 1

        if balance < 0:
            return False

    return balance == 0