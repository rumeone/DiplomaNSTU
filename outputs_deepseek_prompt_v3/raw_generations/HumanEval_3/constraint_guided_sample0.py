from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Determine if a bank account balance falls below zero during a series of operations.

    The account starts with a zero balance. Each operation is an integer representing
    a deposit (positive) or withdrawal (negative). The function returns True if at any
    point the balance becomes negative, otherwise False.

    Args:
        operations: List of deposit and withdrawal amounts.

    Returns:
        True if balance ever falls below zero, False otherwise.

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