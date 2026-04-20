from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string possibly containing multiple groups of nested parentheses.
    Your goal is to separate those groups into separate strings and return the list of those.
    Ignore anything other than "(" and ")" in the input string.
    """
    result = []
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
                result.append(''.join(current_group))
                current_group = []
        # Ignore all other characters as specified

    return result