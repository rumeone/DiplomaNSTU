from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string possibly containing multiple groups of nested parentheses.
    Your goal is to separate those groups into separate strings and return the list of those.
    Ignore anything other than "(" and ")" in the input string.
    """
    result = []
    current_group = []
    balance = 0

    for char in paren_string:
        if char == '(':
            balance += 1
            current_group.append(char)
        elif char == ')':
            balance -= 1
            current_group.append(char)
            # Check for invalid nesting (more closing than opening)
            if balance < 0:
                # Reset to handle malformed input gracefully
                current_group = []
                balance = 0
                continue
            # When balance reaches 0, we have a complete group
            if balance == 0 and current_group:
                result.append(''.join(current_group))
                current_group = []
        # Ignore all other characters as per specification

    # Handle any remaining complete group (shouldn't happen with valid input)
    if balance == 0 and current_group:
        result.append(''.join(current_group))

    return result