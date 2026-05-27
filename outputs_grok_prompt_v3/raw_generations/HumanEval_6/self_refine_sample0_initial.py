"""
Parse maximum nesting depths of parenthesis groups in a string.
"""

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string containing "(" and ")"s (not exclusively),
    possibly including multiple groups for nested parentheses.
    For each of these groups, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three and )( has zero.

    Example:
        >>> parse_nested_parens('{\"example\": \"(()[]()) ((()))()((())()() )\"}')
        [2, 3, 1, 3]
    """
    results = []
    current_depth = 0
    max_depth = 0
    for char in paren_string:
        if char == "(":
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
        elif char == ")":
            current_depth -= 1
            if current_depth == 0:
                results.append(max_depth)
                max_depth = 0
    return results