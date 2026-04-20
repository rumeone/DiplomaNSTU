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
    current_depth = 0
    max_depth = 0
    in_group = False
    
    for char in paren_string:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
            in_group = True
        elif char == ')':
            if current_depth > 0:
                current_depth -= 1
            # If we're at depth 0 after closing and were in a group, record max_depth
            if current_depth == 0 and in_group:
                result.append(max_depth)
                max_depth = 0
                in_group = False
        else:
            # For non-parenthesis characters, if we're at depth 0 and were in a group,
            # it marks the end of a group
            if current_depth == 0 and in_group:
                result.append(max_depth)
                max_depth = 0
                in_group = False
    
    # Handle case where string ends while still in a group
    if in_group:
        result.append(max_depth)
    
    return result