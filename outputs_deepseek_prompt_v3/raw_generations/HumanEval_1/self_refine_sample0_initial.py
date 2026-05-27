from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate a string containing multiple groups of nested parentheses into
    individual balanced parenthesis groups.

    The function ignores any characters other than '(' and ')'. Each returned
    string contains a single balanced parenthesis group.

    Args:
        paren_string: A string potentially containing multiple parenthesis groups.

    Returns:
        A list of strings, each representing a balanced parenthesis group.

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
            current_group.append(char)
            balance += 1
        elif char == ')':
            current_group.append(char)
            balance -= 1

            if balance == 0 and current_group:
                groups.append(''.join(current_group))
                current_group = []

    return groups