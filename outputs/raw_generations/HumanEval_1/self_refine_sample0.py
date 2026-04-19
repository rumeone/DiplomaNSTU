from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    current_group = []
    depth = -1

    for char in paren_string:
        if char == '(':
            if depth == -1:
                depth = 0
            depth += 1
            current_group.append(char)
        elif char == ')':
            depth -= 1
            current_group.append(char)
            if depth == 0:
                groups.append(''.join(current_group))
                current_group = []
                depth = -1

    return groups