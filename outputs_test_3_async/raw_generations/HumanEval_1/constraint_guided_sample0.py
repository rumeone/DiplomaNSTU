"""
Module for separating nested parentheses groups from a string.
"""

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate multiple groups of nested parentheses into individual strings.

    Args:
        paren_string: A string possibly containing multiple groups of nested parentheses.

    Returns:
        A list of strings, each containing a complete group of parentheses.

    Examples:
        >>> separate_paren_groups('(()())')
        ['(()())']
        >>> separate_paren_groups('()(())')
        ['()', '(())']
        >>> separate_paren_groups(')( [) (( ))] (({})( ))')
        ['()', '(())', '(()())']
    """
    result = []
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
                result.append(''.join(current_group))
                current_group = []

    return result