from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string containing multiple groups of parentheses and return
    the maximum nesting depth for each group.

    Args:
        paren_string: A string containing groups of parentheses separated
                     by spaces. The string may contain other characters.

    Returns:
        A list of integers where each integer represents the maximum
        nesting depth of parentheses in each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())())')
        [2, 3, 0, 3]
    """
    results = []
    current_depth = 0
    max_depth = 0
    in_group = False

    for char in paren_string:
        if char == '(':
            current_depth += 1
            in_group = True
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            if current_depth > 0:
                current_depth -= 1
        elif char == ' ':
            if in_group:
                results.append(max_depth)
                current_depth = 0
                max_depth = 0
                in_group = False

    if in_group:
        results.append(max_depth)

    return results