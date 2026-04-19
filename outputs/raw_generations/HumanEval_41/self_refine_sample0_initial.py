def car_race_collision(n: int) -> int:
    """
    Each left-to-right car will collide with all right-to-left cars that start to its right.
    For n cars in each direction, the total collisions is n * n = n².
    """
    return n * n