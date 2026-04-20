from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
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
            if current_depth == 0 and in_group:
                result.append(max_depth)
                max_depth = 0
                in_group = False
        elif char == ' ' and in_group and current_depth == 0:
            result.append(max_depth)
            max_depth = 0
            in_group = False
    
    if in_group:
        result.append(max_depth)
    
    return result