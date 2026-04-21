"""Module providing functions to evaluate polynomials and find their roots."""

import math
from typing import List


def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))


def find_zero(xs: List[int]) -> float:
    """
    xs are coefficients of a polynomial.
    Find x such that poly(x) = 0 and return only one zero point, even if there are many.

    Constraints:
        List xs should have an even number of coefficients
        and as largest a non-zero coefficient to guarantee a solution.

    Examples:
        >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
        -0.5
        >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
        1.0
    """
    # Use binary search to find a root. Since the polynomial has even degree
    # and positive leading coefficient, it goes to +inf as x -> +/- inf.
    # We search in the interval [-1000, 1000] which is guaranteed to contain
    # at least one root given the problem constraints.

    def evaluate(x: float) -> float:
        return poly(xs, x)

    low = -1000.0
    high = 1000.0
    epsilon = 1e-7

    # Ensure we start with opposite signs or zero at one endpoint
    while high - low > epsilon:
        mid = (low + high) / 2.0
        if evaluate(mid) == 0.0:
            return mid
        if evaluate(low) * evaluate(mid) < 0.0:
            high = mid
        else:
            low = mid

    return (low + high) / 2.0