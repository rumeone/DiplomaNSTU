def fibfib(n: int) -> int:
    """
    Compute the n-th FibFib number.
    
    The FibFib sequence is defined as:
    fibfib(0) = 0
    fibfib(1) = 0
    fibfib(2) = 1
    fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3) for n >= 3
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    
    if n < 0:
        raise ValueError("n must be non-negative")
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    
    # Initialize first three values
    a, b, c = 0, 0, 1  # fibfib(0), fibfib(1), fibfib(2)
    
    # Compute iteratively
    for _ in range(3, n + 1):
        next_val = a + b + c
        a, b, c = b, c, next_val
    
    return c