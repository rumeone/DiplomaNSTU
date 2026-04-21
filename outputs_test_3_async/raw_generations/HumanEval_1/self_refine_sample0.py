"""Separate balanced parentheses groups from a string."""

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate balanced parentheses groups from a string.

    Args:
        paren_string: A string possibly containing multiple groups of
            nested parentheses along with other characters.

    Returns:
        A list of strings, each containing a balanced parentheses group.
        Non-parentheses characters are ignored.

    Examples:
        >>> separate_paren_groups('(()())')
        ['(()())']
        >>> separate_paren_groups('()(())')
        ['()', '(())']
        >>> separate_paren_groups(')( [) (( ))] (({})( ))')
        ['()', '(())', '(()())']
    """
    groups = []
    current_group = []
    balance = 0

    for char in paren_string:
        if char == '(':
            balance += 1
            current_group.append(char)
        elif char == ')':
            balance -= 1
            current_group.append(char)
            if balance == 0 and current_group:
                groups.append(''.join(current_group))
                current_group = []

    return groups