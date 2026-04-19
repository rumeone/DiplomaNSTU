from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
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