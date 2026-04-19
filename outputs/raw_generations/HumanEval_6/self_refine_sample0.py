from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
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
                if current_depth == 0 and in_group:
                    results.append(max_depth)
                    max_depth = 0
                    in_group = False
            else:
                if in_group:
                    results.append(max_depth)
                    max_depth = 0
                    in_group = False
        else:
            if current_depth == 0 and in_group:
                results.append(max_depth)
                max_depth = 0
                in_group = False

    if in_group:
        results.append(max_depth)

    return results