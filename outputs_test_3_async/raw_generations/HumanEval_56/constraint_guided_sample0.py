"""
Module for checking if brackets in a string are correctly matched.
"""


def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket has a corresponding closing bracket.

    The function processes a string containing only '<' and '>' characters.
    It ensures that at no point do closing brackets outnumber opening brackets
    and that the total counts match at the end.

    Args:
        brackets: A string consisting of '<' and '>' characters.

    Returns:
        True if brackets are correctly matched, False otherwise.

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

    for bracket in brackets:
        if bracket == "<":
            balance += 1
        elif bracket == ">":
            balance -= 1

        if balance < 0:
            return False

    return balance == 0