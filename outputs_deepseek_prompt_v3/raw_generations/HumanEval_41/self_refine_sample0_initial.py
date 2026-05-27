"""
Module for calculating collision count in a car race scenario.
"""


def car_race_collision(n: int) -> int:
    """
    Calculate the total number of collisions between two sets of cars.

    There are n cars moving left to right and n cars moving right to left.
    Cars continue moving after collisions. Each left-to-right car collides
    with each right-to-left car exactly once.

    Args:
        n: Number of cars in each direction.

    Returns:
        Total number of collisions.
    """
    return n * n