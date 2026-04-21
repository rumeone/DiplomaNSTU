"""
Parse nested parentheses strings to find maximum nesting depth for each group.
"""

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    For each group of parentheses in the input string, find the maximum nesting depth.

    Args:
        paren_string: String containing parentheses groups separated by spaces.

    Returns:
        List of maximum nesting depths for each parentheses group.

    Example:
        >>> parse_nested_parens('(()()) ((())) (())')
        [2, &, 2]
    """
    depths = []
    current_depth = 0
    max_depth = 0
    in_group = False

    for char in paren_string:
        if char == '(':
            in_group = True
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            if current_depth > 0:
                current_depth -= 1
            if current_depth == 0 and in_group:
                depths.append(max_depth)
                max_depth = 0
                in_group = False
        elif char == ' ':
            if in_group and current_depth > 0:
                depths.append(max_depth)
                max_depth = 0
                current_depth = -1
                in_group = False

    if in_group:
        depths.append(max_depth)

    return depths