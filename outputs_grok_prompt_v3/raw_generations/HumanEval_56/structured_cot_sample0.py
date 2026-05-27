"""Bracket balancing utilities."""

def correct_bracketing(brackets: str) -> bool:
    """
    brackets is a string of "<" and ">".
    Check if every opening bracket has a corresponding closing bracket.

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
    count = 0
    for char in brackets:
        if char == "<":
            count += 1
        elif char == ">":
            count -= 1
        if count < 0:
            return False
    return count == 0