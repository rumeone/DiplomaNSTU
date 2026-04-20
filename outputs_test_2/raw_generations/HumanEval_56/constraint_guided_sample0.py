"""
Check if a string of angle brackets has correctly matched pairs.
"""


def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket '<' has a corresponding closing bracket '>'.

    Args:
        brackets: A string containing only '<' and '>' characters.

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

        # If balance becomes negative, we have a closing bracket without an opener
        if balance < 0:
            return False

    # All brackets are matched if balance is zero
    return balance == 0