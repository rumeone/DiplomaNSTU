def largest_divisor(n: int) -> int:
    """
    Find the largest number that divides n evenly, smaller than n.
    Return -1 if such a number does not exist.
    """
    if n <= 1:
        return -1
    
    for d in range(n - 1, 0, -1):
        if n % d == 0:
            return d
    
    return -1