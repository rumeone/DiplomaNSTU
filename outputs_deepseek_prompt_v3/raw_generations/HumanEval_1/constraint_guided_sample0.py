from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Extract and separate balanced parenthesis groups from a string.
    
    The function processes the input string character by character, ignoring
    any characters other than '(' and ')'. It identifies complete balanced
    parenthesis groups and returns them as a list of strings.
    
    Args:
        paren_string: A string potentially containing multiple parenthesis groups.
        
    Returns:
        A list of strings, each representing a complete balanced parenthesis group.
        
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
            elif balance < 0:
                # Reset on unmatched closing parenthesis
                current_group = []
                balance = 0
    
    return groups