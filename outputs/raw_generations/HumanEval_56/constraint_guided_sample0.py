def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket '<' has a corresponding closing bracket '>'
    and that they are correctly nested/paired.
    """
    balance = 0
    for ch in brackets:
        if ch == '<':
            balance += 1
        elif ch == '>':
            balance -= 1
            # If balance goes negative, a closing bracket appears before an opening one.
            if balance < 0:
                return False
    # At the end, balance must be zero for all brackets to be correctly paired.
    return balance == 0