"""
Module for calculating car race collisions on an infinite straight road.

This module provides a function to determine the total number of collisions
between two sets of n cars moving in opposite directions.
"""


def car_race_collision(n: int) -> int:
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right; simultaneously, a different set of n cars
    are driving right to left.

    n cars -> ..... <- n other cars

    The two sets of cars start out being very far from
    each other. All cars move in the same speed. Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the total number of such collisions possible given n.

    The key insight is that because the cars continue moving as if they didn't collide
    (they pass through each other), every left-moving car will eventually collide
    with every right-moving car exactly once.

    Args:
        n: The number of cars in each direction.

    Returns:
        The total number of collisions, which is n * n.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    return n * n