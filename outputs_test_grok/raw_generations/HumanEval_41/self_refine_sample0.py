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
    each other and continue their trajectories unchanged. The total number of
    collisions equals the number of unique pairs where one car from each group
    will meet.

    Args:
        n: The number of cars in each direction.

    Returns:
        The total number of collisions, which is n squared.
    """
    if n <= 0:
        return 0

    return n * n