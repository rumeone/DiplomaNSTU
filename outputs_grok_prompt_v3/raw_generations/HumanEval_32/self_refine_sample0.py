"""Module providing polynomial evaluation and root-finding utilities."""

import math
from typing import List


def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))


def find_zero(xs: List[int]) -> float:
    """
    xs are coefficients of a polynomial.
    Find x such that poly(x) = 0 and return only one zero point, even if there are many.

    Constraints:
        List xs should have an even number of coefficients
        and as largest a non-zero coefficient to guarantee a solution.
    """
    # Use bisection method on an interval guaranteed to contain a root
    lower_bound, upper_bound = -1.0, 1.0
    while poly(xs, lower_bound) * poly(xs, upper_bound) > 0:
        lower_bound *= 2
        upper_bound *= 2

    for _ in range(10000):
        midpoint = (lower_bound + upper_bound) / 2
        if poly(xs, midpoint) * poly(xs, lower_bound) > 0:
            lower_bound = midpoint
        else:
            upper_bound = midpoint

    return lower_bound