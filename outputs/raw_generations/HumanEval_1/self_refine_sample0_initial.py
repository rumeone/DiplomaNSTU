def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    current_group = []
    depth = 0
    
    for char in paren_string:
        if char == '(':
            depth += 1
            current_group.append(char)
        elif char == ')':
            depth -= 1
            current_group.append(char)
            if depth == 0:
                groups.append(''.join(current_group))
                current_group = []
    
    return groups