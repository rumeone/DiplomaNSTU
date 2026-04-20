def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket has a corresponding closing bracket.
    """
    balance = 0
    for char in brackets:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            # If balance becomes negative, a closing bracket appears before an opening one
            if balance < 0:
                return False
    # Valid if all brackets are balanced
    return balance == 0