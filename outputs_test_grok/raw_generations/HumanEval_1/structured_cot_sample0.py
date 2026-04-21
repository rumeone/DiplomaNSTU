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
    result: List[str] = []
    stack: List[int] = []
    start = -1

    for i, char in enumerate(paren_string):
        if char == "(":
            if not stack:
                start = i
            stack.append(i)
        elif char == ")":
            if stack:
                stack.pop()
                if not stack and start != -1:
                    result.append(paren_string[start : i + 1])
                    start = -1

    return result