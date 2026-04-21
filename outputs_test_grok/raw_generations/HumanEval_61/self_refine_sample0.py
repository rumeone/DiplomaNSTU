"""
Module providing a function to check if brackets are correctly matched.
"""


def correct_bracketing(brackets: str) -> bool:
    """
    Check if every opening bracket has a corresponding closing bracket.

    brackets is a string consisting only of "(" and ")".

    Returns True if the brackets are correctly matched (balanced),
    False otherwise.

    Examples:
        >>> correct_bracketing("(")
        False
        >>> correct_bracketing("()")
        True
        >>> correct_bracketing("(()())")
        True
        >>> correct_bracketing(")(()")
        False
    """
    if not brackets:
        return True

    balance = 0
    for char in brackets:
        if char == "(":
            balance += 1
        else:  # char == ")"
            balance -= 1

        if balance < 0:
            return False

    return balance == 0