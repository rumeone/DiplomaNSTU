def correct_bracketing(brackets: str) -> bool:
    """
    Return True if every opening bracket '<' has a matching closing bracket '>'
    in correct order, otherwise False.
    """
    balance = 0
    for ch in brackets:
        if ch == '<':
            balance += 1
        elif ch == '>':
            balance -= 1
        # If balance becomes negative, a closing bracket appears before an opening one.
        if balance < 0:
            return False
    # At the end, balance must be zero.
    return balance == 0