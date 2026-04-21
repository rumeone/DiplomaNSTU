"""
Module for checking bracket correctness in a string of '<' and '>' characters.

This module provides a function to validate whether every opening bracket
has a corresponding closing bracket, following proper nesting rules.
"""


def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket has a corresponding closing bracket.

    The function uses a counter to track the balance of brackets.
    It returns False immediately if a closing bracket appears without
    a matching opening bracket. At the end, it checks if all brackets
    are properly closed.

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
    open_count = 0

    for char in brackets:
        if char == "<":
            open_count += 1
        elif char == ">":
            if open_count == 0:
                return False
            open_count -= 1

    return open_count == 0