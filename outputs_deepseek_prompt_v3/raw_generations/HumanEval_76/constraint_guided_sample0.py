"""
Check if a number is a simple power of another number.
"""


def is_simple_power(x: int, n: int) -> bool:
    """
    Check if number x is a simple power of n.
    
    x is a simple power of n if n to the power of some integer equals x.
    
    Examples:
        is_simple_power(1, 4) => True (4^0 = 1)
        is_simple_power(2, 2) => True (2^1 = 2)
        is_simple_power(8, 2) => True (2^3 = 8)
        is_simple_power(3, 2) => False (only 2 and 4 are neighbouring simple powers)
        is_simple_power(3, 1) => False (1 is not a simple power of any number besides itself)
    
    Args:
        x: The number to check.
        n: The base number.
    
    Returns:
        True if x is a simple power of n, False otherwise.
    """
    # Handle edge cases
    if x == 1:
        # 1 is n^0 for any n except 0, but we need to check if n is valid
        return n != 0 and n != 1  # Special case: 1 is not a simple power of 1 (except 1^1)
    
    if n <= 1:
        # For n <= 1, only x == n is a valid simple power
        return x == n
    
    if x <= 0:
        # Non-positive numbers are not simple powers (except maybe 1 handled above)
        return False
    
    # Check if x is a power of n
    current_power = 1
    while current_power <= x:
        if current_power == x:
            return True
        current_power *= n
    
    return False