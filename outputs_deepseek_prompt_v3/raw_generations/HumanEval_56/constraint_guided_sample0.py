"""
Module for checking bracket balancing in strings containing only '<' and '>'.
"""


def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket '<' has a corresponding closing bracket '>'.

    The function validates that brackets are properly paired and ordered:
    - Each opening bracket must have a matching closing bracket
    - Closing brackets cannot appear before their corresponding opening brackets

    Args:
        brackets: A string containing only '<' and '>' characters.

    Returns:
        True if brackets are correctly paired and ordered, False otherwise.

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

        # If balance goes negative, we have a closing bracket without opening
        if balance < 0:
            return False

    # All brackets are balanced if balance is zero
    return balance == 0