"""
Detect if a bank account balance falls below zero during a series of operations.
"""

from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Check if the account balance ever falls below zero during the operations.

    Args:
        operations: List of deposit (positive) and withdrawal (negative) operations.

    Returns:
        True if balance falls below zero at any point, False otherwise.

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