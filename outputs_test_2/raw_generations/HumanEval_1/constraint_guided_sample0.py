"""
Module for separating nested parentheses groups from a string.
"""

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a string.

    The function extracts all balanced groups of parentheses from the input string,
    ignoring any characters other than '(' and ')'. Each balanced group is returned
    as a separate string in a list.

    Args:
        paren_string: A string possibly containing multiple groups of parentheses.

    Returns:
        A list of strings, each representing a balanced parentheses group.

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