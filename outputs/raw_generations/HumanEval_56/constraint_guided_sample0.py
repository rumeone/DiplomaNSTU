def correct_bracketing(brackets: str) -> bool:
    """
    brackets is a string of "<" and ">".
    Check if every opening bracket has a corresponding closing bracket.
    """
    balance = 0
    for ch in brackets:
        if ch == "<":
            balance += 1
        elif ch == ">":
            balance -= 1
        # If balance becomes negative, a closing bracket appears before an opening one
        if balance < 0:
            return False
    # At the end, balance should be zero for correct bracketing
    return balance == 0