"""
Module for calculating car race collisions on an infinite straight road.

This module provides a function to determine the total number of collisions
between two groups of cars moving in opposite directions.
"""


def car_race_collision(n: int) -> int:
    """
    Calculate the total number of collisions between n cars moving right
    and n cars moving left on an infinite straight road.

    All cars move at the same speed. When two cars collide, they pass
    through each other and continue their trajectories unchanged. This
    means each right-moving car will eventually collide with every
    left-moving car.

    Args:
        n: The number of cars in each direction.

    Returns:
        The total number of collisions, which is n * n.

    Examples:
        >>> car_race_collision(1)
        1
        >>> car_race_collision(2)
        4
        >>> car_race_collision(3)
        9
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return n * n