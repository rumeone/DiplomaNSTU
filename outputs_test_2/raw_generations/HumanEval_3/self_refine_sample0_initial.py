from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Detect if at any point the bank account balance falls below zero.
    The account starts with zero balance and processes a list of deposit
    and withdrawal operations. Returns True if balance ever goes negative,
    False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False