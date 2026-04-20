from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string containing "(" and ")"s (not exclusively),
    possibly including multiple groups for nested parentheses.
    For each of these groups, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three and )( has zero.
    """
    results = []
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
                # End of group when we return to depth 0
                if current_depth == 0 and in_group:
                    results.append(max_depth)
                    max_depth = 0
                    in_group = False
            else:
                # Handle unmatched closing parenthesis
                if in_group:
                    results.append(max_depth)
                max_depth = 0
                in_group = False
        else:
            # Non-parenthesis character at depth 0 means we're between groups
            if current_depth == 0 and in_group:
                results.append(max_depth)
                max_depth = 0
                in_group = False

    # Handle case where string ends while still in a valid group
    if in_group and current_depth == 0:
        results.append(max_depth)

    return results