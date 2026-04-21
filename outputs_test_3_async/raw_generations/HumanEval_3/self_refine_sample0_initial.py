"""
Detect if a bank account balance falls below zero during a series of operations.
"""

from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Check if the balance ever falls below zero during deposit/withdrawal operations.

    The account starts with zero balance. Each integer in the operations list
    represents a deposit (positive) or withdrawal (negative). The function
    returns True if at any point the balance becomes negative, otherwise False.

    Args:
        operations: List of integers representing deposit and withdrawal amounts.

    Returns:
        bool: True if balance falls below zero at any point, False otherwise.

    Examples:
        >>> below_zero([1, 2, 3])
        False
        >>> below_zero([1, 2, -4, 5])
        True
    """
    balance = 0

    for operation in operations:
        balance += operation
        if balance < 0:
            return True

    return False