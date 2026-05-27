"""Separate groups of nested parentheses from a string."""

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string possibly containing multiple groups of nested parentheses.
    Your goal is to separate those groups into separate strings and return the list of those.
    Ignore anything other than "(" and ")" in the input string.

    Examples:
        >>> seperate_paren_groups('(()())')
        ['(()())']
        >>> separate_paren_groups('()(())')
        ['()', '(())']
        >>> separate_paren_groups(')( [) (( ))] (({})( ))')
        ['()', '(())', '(()())']
    """
    groups: List[str] = []
    current_group = ""
    depth = 0

    for char in paren_string:
        if char == "(":
            current_group += char
            depth += 1
        elif char == ")" and depth > 0:
            current_group += char
            depth -= 1
            if depth == 0:
                groups.append(current_group)
                current_group = ""

    return groups