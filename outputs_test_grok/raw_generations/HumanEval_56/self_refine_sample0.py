"""
Module providing a function to check if brackets are correctly matched.
"""


def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket has a corresponding closing bracket.

    brackets is a string of "<" and ">".

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

    open_count = 0
    for char in brackets:
        if char == "<":
            open_count += 1
        elif char == ">":
            open_count -= 1
            if open_count < 0:
                return False

    return open_count == 0