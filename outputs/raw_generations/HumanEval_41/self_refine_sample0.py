def car_race_collision(n: int) -> int:
    """
    Calculate the total number of collisions between two sets of n cars
    moving in opposite directions on an infinite straight road.
    
    Since all cars move at the same speed and are infinitely sturdy,
    each left-to-right car will pass through every right-to-left car,
    resulting in one collision per pair.
    
    Args:
        n: Number of cars moving in each direction (non-negative integer).
    
    Returns:
        Total number of collisions (n²).
    
    Raises:
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    
    return n * n