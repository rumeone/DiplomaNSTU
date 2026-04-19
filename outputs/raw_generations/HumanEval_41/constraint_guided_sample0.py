def car_race_collision(n: int) -> int:
    """
    Each left-to-right car will collide with every right-to-left car
    that starts to its left. Since all cars move at the same speed and
    start far apart, collisions occur when a left-to-right car and a
    right-to-left car pass each other. This is equivalent to counting
    all ordered pairs (left_car, right_car) where left_car is to the
    left of right_car initially. With n cars each direction, this is n * n.
    """
    return n * n