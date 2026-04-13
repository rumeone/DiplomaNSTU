from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
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
            # If we were in a group and now depth is 0, group ended
            if in_group and current_depth == 0:
                result.append(max_depth)
                max_depth = 0
                in_group = False
        else:
            # For non-parenthesis characters, if we were in a group and depth is 0, end group
            if in_group and current_depth == 0:
                result.append(max_depth)
                max_depth = 0
                in_group = False
    
    # Handle case where string ends while still in a group
    if in_group:
        result.append(max_depth)
    
    return result