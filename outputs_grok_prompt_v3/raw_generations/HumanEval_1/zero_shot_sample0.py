def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    current_group = []
    balance = 0
    for char in paren_string:
        if char == "(":
            balance += 1
            current_group.append(char)
        elif char == ")" and balance > 0:
            balance -= 1
            current_group.append(char)
            if balance == 0:
                groups.append("".join(current_group))
                current_group = []
    return groups