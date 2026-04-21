"""Parse nested parentheses to find maximum nesting depth per group."""

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
    depths: List[int] = []
    current_depth = 0
    max_depth = 0
    in_group = False

    for char in paren_string:
        if char == "(":
            if not in_group:
                in_group = True
                current_depth = 0
                max_depth = 0
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
        elif char == ")":
            if in_group:
                current_depth -= 1
                if current_depth < 0:
                    current_depth = 0
        else:
            # Non-parenthesis character ends the current group if we're in one
            if in_group:
                depths.append(max_depth)
                in_group = False
                current_depth = 0
                max_depth = 0

    # Handle the case where the string ends with an open group
    if in_group:
        depths.append(max_depth)

    return depths