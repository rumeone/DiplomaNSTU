"""
Module for checking bracket correctness in a string of '<' and '>' characters.

This module provides a function to validate whether every opening bracket
has a corresponding closing bracket, following proper nesting rules.
"""


def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket has a corresponding closing bracket.

    The function uses a counter to track the balance of brackets.
    It returns False immediately if a closing bracket appears before
    any opening bracket or if the final count is not zero.

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
    if not brackets:
        return True

    balance = 0
    for char in brackets:
        if char == "<":
            balance += 1
        elif char == ">":
            balance -= 1
            if balance < 0:
                return False
        else:
            # Ignore any unexpected characters as per problem focus
            continue

    return balance == 0