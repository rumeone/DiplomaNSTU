from collections import deque


def correct_bracketing(brackets: str) -> bool:
    """
    brackets is a string of "(" and ")".
    Check if every opening bracket has a corresponding closing bracket.

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
    stack: deque[int] = deque()
    for char in brackets:
        if char == "(":
            stack.append(1)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0