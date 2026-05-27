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
    current_chars: List[str] = []
    balance = 0
    for char in paren_string:
        if char == "(":
            balance += 1
            current_chars.append(char)
        elif char == ")":
            if balance > 0:
                balance -= 1
                current_chars.append(char)
                if balance == 0:
                    groups.append("".join(current_chars))
                    current_chars = []
    return groups