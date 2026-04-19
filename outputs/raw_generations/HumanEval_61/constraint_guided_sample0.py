def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket has a corresponding closing bracket.
    Returns True if the brackets are correctly balanced, False otherwise.
    """
    balance = 0
    for char in brackets:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            # If balance becomes negative, we have a closing bracket without a matching opening bracket
            if balance < 0:
                return False
    # At the end, balance should be zero for correct bracketing
    return balance == 0