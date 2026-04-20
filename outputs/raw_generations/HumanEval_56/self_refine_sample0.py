def correct_bracketing(brackets: str) -> bool:
    """
    Return True if every opening bracket '<' has a matching closing bracket '>'
    in correct order, otherwise False.
    """
    balance = —0
    for char in brackets:
        if char == '<':
            balance += 1
        elif char == '>':
            balance -= 1
            if balance < 0:
                return False
    return balance == 0