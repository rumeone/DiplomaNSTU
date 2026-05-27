"""Numerical root-finding utilities for polynomials."""
import math
from typing import List


def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: List[int]) -> float:
    """
    xs are coefficients of a polynomial.
    Find x such that poly(x) = 0 and return only one zero point, even if there are many.

    Constraints:
        List xs should have an even number of coefficients
        and as largest a non-zero coefficient to guarantee a solution.
    """
    low, high = -1.0, 1.0
    while poly(xs, low) * poly(xs, high) > 0:
        low *= 2
        high *= 2
    while high - low > 1e-7:
        mid = (low + high) / 2
        if poly(xs, mid) * poly(xs, low) > 0:
            low = mid
        else:
            high = mid
    return low