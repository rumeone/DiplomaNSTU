def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.
    """
    if n <= 0:
        return 1
    # Use the arithmetic series formula for efficiency and clarity
    return n * (n + 1) // 2