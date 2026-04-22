"""Parse strings containing nested parentheses and report maximum nesting depth per group."""

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
    if not paren_string:
        return []

    depths = []
    current_depth = 0
    max_depth = 0
    in_group = False

    for char in paren_string:
        if char == "(":
            in_group = True
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
        elif char == ")":
            in_group = True
            current_depth = max(0, current_depth - 1)
        elif char.isspace() or char in ",:[]{}'\"":
            # End of a group when we encounter whitespace or structural characters
            # after having seen parentheses
            if in_group:
                depths.append(max_depth)
                current_depth = 0
                max_depth = 0
                in_group = False
        else:
            # Other characters are ignored but reset group state if we were in one
            if in_group:
                depths.append(max_depth)
                current_depth = 0
                max_depth = 0
                in_group = False

    # Handle the last group if the string didn't end with a separator
    if in_group or max_depth > 0 or current_depth > 0:
        depths.append(max_depth)

    return depths