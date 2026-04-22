"""Module for detecting negative bank account balances.

This module provides a function to check if a sequence of bank operations
ever causes the account balance to fall below zero.
"""


from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Detect if the bank account balance falls below zero at any point.

    The account starts with a zero balance. For each operation in the list,
    a positive number represents a deposit and a negative number represents
    a withdrawal. The function returns True as soon as the balance becomes
    negative, otherwise it returns False after processing all operations.

    Args:
        operations: List of deposit (positive) and withdrawal (negative) amounts.

    Returns:
        True if balance goes below zero at any point, False otherwise.

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