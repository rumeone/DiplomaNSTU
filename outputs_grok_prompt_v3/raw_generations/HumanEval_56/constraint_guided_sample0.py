"""Utility for validating balanced angle bracket sequences."""

def correct_bracketing(brackets: str) -> bool:
    """
    brackets is a string of "<" and ">".
    Check if every opening bracket has a corresponding closing bracket.
    """
    balance = 0
    for char in brackets:
        if char == "<":
            balance += 1
        elif char == ">":
            balance -= 1
        if balance < 0:
            return False
    return balance == 0