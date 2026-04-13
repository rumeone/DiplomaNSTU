from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    results = []
    current_depth = 0
    max_depth = 0
    
    for char in paren_string:
        if char == '(':
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
        elif char == ')':
            current_depth -= 1
            if current_depth < 0:
                # Invalid closing parenthesis - reset for next group
                current_depth = 0
                max_depth = 0
        elif char == ' ':
            # Space indicates end of a group
            if max_depth > 0 or current_depth == 0:
                results.append(max_depth)
            current_depth = 0
            max_depth = 0
    
    # Handle last group if string doesn't end with space
    if max_depth > 0 or current_depth == 0:
        results.append(max_depth)
    
    return results