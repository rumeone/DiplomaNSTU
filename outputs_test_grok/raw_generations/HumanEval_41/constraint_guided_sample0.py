"""
Module for calculating car race collisions on an infinite straight road.

This module provides a function to determine the total number of collisions
between two sets of n cars moving in opposite directions.
"""


def car_race_collision(n: int) -> int:
    """
    Calculate the total number of collisions between n cars moving left to right
    and n cars moving right to left on an infinite straight road.

    All cars move at the same speed. When two cars collide, they pass through
    each other and continue their trajectories unchanged. This means each car
    from the left-to-right group will eventually collide with every car from
    the right-to-left group.

    Args:
        n: The number of cars in each direction. Must be a non-negative integer.

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
    if n <= 0:
        return 0

    return n * n