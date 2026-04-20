def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.
    """
    if n < 0:
        return 0
    # Use the arithmetic series formula for efficiency
    return n * (n + 1) // 2