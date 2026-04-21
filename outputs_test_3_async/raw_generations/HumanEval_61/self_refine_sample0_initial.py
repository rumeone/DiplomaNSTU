"""
Module for checking correctness of bracket sequences.

The main function correct_bracketing verifies if every opening bracket
in a string has a corresponding closing bracket in the correct order.
"""


def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket has a corresponding closing bracket.

    Args:
        brackets: A string consisting only of '(' and ')' characters.

    Returns:
        True if the brackets are correctly matched and balanced,
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

    for char in brackets:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1

            if balance < 0:
                return False

    return balance == 0