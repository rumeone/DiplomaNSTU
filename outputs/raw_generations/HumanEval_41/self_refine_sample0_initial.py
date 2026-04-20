def car_race_collision(n: int) -> int:
    """
    Each left-to-right car will collide with every right-to-left car it meets.
    Since all cars move at the same speed and start far apart, each left-to-right
    car will eventually pass all right-to-left cars coming from the opposite direction.
    Therefore, each of the n left-to-right cars collides with all n right-to-left cars.
    Total collisions = n * n = n^2.
    """
    return n * n