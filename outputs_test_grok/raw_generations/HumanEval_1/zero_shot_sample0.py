from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string possibly containing multiple groups of nested parentheses.
    Your goal is to separate those groups into separate strings and return the list of those.
    Ignore anything other than "(" and ")" in the input string.
    """
    result = []
    stack = []
    current = []
    for char in paren_string:
        if char == '(':
            stack.append('(')
            current.append('(')
        elif char == ')':
            if stack:
                stack.pop()
                current.append(')')
                if not stack:
                    result.append(''.join(current))
                    current = []
    return result