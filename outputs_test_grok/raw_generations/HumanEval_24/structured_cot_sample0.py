def largest_divisor(n: int) -> int:
    """
    Find the largest number that divides n evenly, smaller than n.
    Return -1 if such a number does not exist.
    """
    if n <= 1:
        return -1
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return -1