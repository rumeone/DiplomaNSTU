"""
This module provides functionality to calculate the number of collisions
in a scenario where two sets of cars are moving in opposite directions.
"""


def car_race_collision(n: int) -> int:
    """
    Calculate the total number of collisions between two sets of cars
    moving in opposite directions.

    Args:
        n: The number of cars moving in each direction.

    Returns:
        The total number of collisions that occur.

    Notes:
        Each car moving left to right will collide with every car moving
        right to left that it encounters. Since all cars move at the same
        speed and start far apart, each left-to-right car will collide with
        all right-to-left cars.
    """
    return n * n