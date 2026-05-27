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
    result = []
    current = []
    balance = 0
    
    for char in paren_string:
        if char == '(':
            current.append(char)
            balance += 1
        elif char == ')':
            current.append(char)
            balance -= 1
            
            if balance == 0:
                result.append(''.join(current))
                current = []
    
    return result