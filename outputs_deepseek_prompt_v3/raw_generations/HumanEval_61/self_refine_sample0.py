"""
Module for checking if brackets are correctly matched.
"""


def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket has a corresponding closing bracket.

    Args:
        brackets: A string consisting only of '(' and ')'.

    Returns:
        True if brackets are correctly matched, False otherwise.
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