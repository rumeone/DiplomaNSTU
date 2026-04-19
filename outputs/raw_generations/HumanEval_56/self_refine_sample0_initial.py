def correct_bracketing(brackets: str) -> bool:
    balance = 0
    for ch in brackets:
        if ch == "<":
            balance += 1
        elif ch == ">":
            balance -= 1
        # If balance becomes negative, a closing bracket appears before an opening one
        if balance < 0:
            return False
    # At the end, balance must be zero for all brackets to be correctly paired
    return balance == 0