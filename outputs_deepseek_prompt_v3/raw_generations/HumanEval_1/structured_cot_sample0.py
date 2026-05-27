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
    filtered_chars = [ch for ch in paren_string if ch in '()']
    groups = []
    current_group = []
    balance = 0

    for ch in filtered_chars:
        current_group.append(ch)
        if ch == '(':
            balance += 1
        else:  # ch == ')'
            balance -= 1
            if balance == 0:
                groups.append(''.join(current_group))
                current_group = []

    return groups