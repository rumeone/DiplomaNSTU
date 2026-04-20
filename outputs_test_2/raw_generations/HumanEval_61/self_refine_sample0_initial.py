"""
Module for checking bracket balancing in strings containing '(' and ')'.
"""


def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket has a corresponding closing bracket.

    The function uses a counter to track the balance of brackets.
    An opening bracket increases the counter, a closing bracket decreases it.
    If the counter ever becomes negative, the string is invalid.
    At the end, the counter must be zero for a valid string.

    Args:
        brackets: A string containing only '(' and ')' characters.

    Returns:
        True if the brackets are correctly balanced, False otherwise.

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