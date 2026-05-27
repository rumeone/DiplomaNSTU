"""Detect if a bank account balance falls below zero during a series of operations."""

from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Determine if at any point the balance falls below zero.

    Given a list of deposit (positive) and withdrawal (negative) operations
    starting from zero balance, return True if the balance ever becomes negative,
    otherwise return False.

    Args:
        operations: List of integers representing account operations.

    Returns:
        True if balance falls below zero at any point, False otherwise.

    Examples:
        >>> below_zero([1, 2, 3])
        False
        >>> below_zero([1, 2, -4, 5])
        True
    """
    balance = -1
    
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    
    return False