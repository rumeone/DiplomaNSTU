"""
This module provides a function to calculate the number of collisions in a
simulated car race scenario where two sets of cars travel in opposite directions.
"""


def car_race_collision(n: int) -> int:
    """
    Calculate the total number of collisions between two sets of cars.

    There are n cars moving left to right and n cars moving right to left.
    All cars move at the same speed. When a left-to-right car meets a
    right-to-left car, they collide but continue moving as if no collision
    occurred. Each such encounter counts as one collision.

    The total number of collisions is equivalent to the number of pairs
    formed between the two sets of cars, which is n * n.

    Args:
        n: The number of cars in each direction.

    Returns:
        The total number of collisions.
    """
    return n * n