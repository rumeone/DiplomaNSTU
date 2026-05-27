"""
Parse nested parentheses strings to find maximum nesting depth for each group.
"""

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string containing multiple groups of parentheses and return
    the maximum nesting depth for each group.

    Args:
        paren_string: String containing parentheses groups separated by spaces.
                     May contain other characters which are ignored.

    Returns:
        List of integers representing maximum nesting depth for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) (()(()))')
        [2, 3, 3]
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
            # If we reach depth 0 and were in a group, record the result
            if current_depth == 0 and in_group:
                results.append(max_depth)
                max_depth = 0
                in_group = False
        elif char == ' ':
            # Handle space-separated groups
            if in_group and current_depth == 0:
                results.append(max_depth)
                max_depth = 0
                in_group = False
            # Reset for new group if we encounter space
            current_depth = 0
            max_depth = 0
            in_group = False

    # Handle case where string ends with a group
    if in_group and current_depth == 0:
        results.append(max_depth)

    return results