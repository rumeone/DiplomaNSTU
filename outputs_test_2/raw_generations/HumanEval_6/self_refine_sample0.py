from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string containing multiple groups of parentheses and return the
    maximum nesting depth for each group.

    Args:
        paren_string: A string containing parentheses groups separated by spaces.
                     May contain other characters which are ignored.

    Returns:
        A list of integers where each integer represents the maximum nesting
        depth of parentheses in each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())())')
        [2, 3, 1, 3]
    """
    result = []
    current_depth = 0
    max_depth = 0
    in_group = False

    for char in paren_string:
        if char == '(':
            current_depth += 1
            in_group = True
            if current_depth > max_depth:
                max_depth = current_depth
        elif char == ')':
            if current_depth > 0:
                current_depth -= 1
            if current_depth == 0 and in_group:
                result.append(max_depth)
                max_depth = 0
                in_group = False
        elif char == ' ':
            if in_group and current_depth == 0:
                result.append(max_depth)
                max_depth = 0
                in_group = False
            current_depth = 0
            max_depth = 0

    if in_group:
        result.append(max_depth)

    return result