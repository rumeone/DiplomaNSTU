from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string containing "(" and ")"s (not exclusively),
    possibly including multiple groups for nested parentheses.
    For each of these groups, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three and )( has zero.

    Example:
        >>> parse_nested_parens('{"example": "(()[]()) ((()))()((())()() )"}')
        [2, 3, 1, 3]
    """
    result = []
    current_max = 0
    current_depth = 0

    for char in paren_string:
        if char == '(':
            current_depth += 1
            current_max = max(current_max, current_depth)
        elif char == ')':
            current_depth -= 1
            if current_depth == 0:
                result.append(current_max)
                current_max = 0
        elif char == ' ' and current_depth == 0:
            continue

    return result