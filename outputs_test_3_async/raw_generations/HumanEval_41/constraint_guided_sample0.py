"""
This module provides a function to compute the number of collisions in a car race scenario.
"""


def car_race_collision(n: int) -> int:
    """
    Calculate the total number of collisions between two sets of cars moving in opposite directions.

    There are n cars moving left to right and n cars moving right to left on an infinite straight road.
    All cars move at the same speed. When a left-to-right car meets a right-to-left car, a collision occurs.
    After collision, cars continue moving as if no collision happened (they pass through each other).

    Since each left-to-right car collides with every right-to-left car exactly once, the total number
    of collisions is n * n = n².

    Parameters
    ----------
    n : int
        The number of cars moving in each direction.

    Returns
    -------
    int
        The total number of collisions.
    """
    return n * n