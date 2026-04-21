"""Module for separating nested parentheses groups from a string."""

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string possibly containing multiple groups of nested parentheses.
    Your goal is to separate those groups into separate strings and return the list of those.
    Ignore anything other than "(" and ")" in the input string.

    Examples:
        >>> separate_paren_groups('(()())')
        ['(()())']
        >>> separate_paren_groups('()(())')
        ['()', '(())']
        >>> separate_paren_groups(')( [) (( ))] (({})( ))')
        ['()', '(())', '(()())']
    """
    if not paren_string:
        return []

    result: List[str] = []
    stack: List[int] = []
    start = -1

    for i, char in enumerate(paren_string):
        if char == "(":
            if not stack:  # Start of a new group
                start = i
            stack.append(i)
        elif char == ")":
            if not stack:
                continue  # Ignore unmatched closing parentheses
            stack.pop()
            if not stack and start != -1:  # Found a complete group
                group = paren_string[start : i + 1]
                result.append(group)
                start = -1

    return result