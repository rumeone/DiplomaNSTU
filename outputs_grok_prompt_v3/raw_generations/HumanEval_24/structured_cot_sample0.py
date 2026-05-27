"""
Find the largest proper divisor of a positive integer.
"""

def largest_divisor(n: int) -> int:
    """
    Find the largest number that divides n evenly, smaller than n.
    Return -1 if such a number does not exist.
    """
    if n <= 1:
        return -1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return n // i
    return 1