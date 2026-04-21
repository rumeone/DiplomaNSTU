"""
Module for checking if brackets in a string are correctly matched.
"""


def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket has a corresponding closing bracket.

    Args:
        brackets: A string consisting only of '(' and ')' characters.

    Returns:
        True if every opening bracket is properly matched with a closing bracket,
        False otherwise.

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
    balance = 0

    for bracket in brackets:
        if bracket == '(':
            balance += 1
        elif bracket == ')':
            balance -= 1

        if balance < 0:
            return False

    return balance == 0