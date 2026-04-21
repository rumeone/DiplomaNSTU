"""Parse nested parentheses strings to find maximum nesting depth for each group."""

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string containing multiple groups of parentheses and return the
    maximum nesting depth for each group.

    Args:
        paren_string: A string containing parentheses groups separated by spaces.
                     The string may contain other characters which are ignored.

    Returns:
        A list of integers where each integer represents the maximum nesting
        depth of parentheses in each group.

    Examples:
        >>> parse_nested_parens('(()()) ((())) (())')
        [2, 3, 2]
        >>> parse_nested_parens('() (())')
        [1, 2]
    """
    result = []
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
            # If we close a group and we're back at depth 0, record the result
            if current_depth == 0 and in_group:
                result.append(max_depth)
                max_depth = 0
                in_group = False
        elif char == ' ' and in_group:
            # Handle malformed groups (unclosed parentheses)
            if current_depth > 0:
                result.append(max_depth)
                current_depth = 0
                max_depth = 0
                in_group = False

    # Handle case where string ends without closing all parentheses
    if in_group and current_depth >= 0:
        result.append(max_depth)

    return result