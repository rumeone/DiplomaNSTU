"""
This module provides a function to calculate the number of collisions in a
simulated car race scenario where cars moving in opposite directions pass
through each other.
"""


def car_race_collision(n: int) -> int:
    """
    Calculate the total number of collisions between cars moving in opposite
    directions.

    In this scenario, there are n cars moving left to right and n cars moving
    right to left on an infinitely long straight road. All cars move at the
    same constant speed. When cars moving in opposite directions meet, they
    collide but continue moving as if nothing happened (they pass through each
    other). Each pair of cars moving in opposite directions will collide exactly
    once.

    Parameters
    ----------
    n : int
        The number of cars moving in each direction.

    Returns
    -------
    int
        The total number of collisions, which is n * n (each left-to-right car
        collides with every right-to-left car).
    """
    return n * n