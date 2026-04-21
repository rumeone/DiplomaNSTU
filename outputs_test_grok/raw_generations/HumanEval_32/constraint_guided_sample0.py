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
    # Use binary search to find a root. The constraints guarantee a real root exists.
    # Since the leading coefficient is non-zero and degree is even, the polynomial
    # tends to +inf or -inf on both sides, but must cross zero due to the problem
    # constraints.

    def evaluate(x: float) -> float:
        return poly(xs, x)

    # Start with a reasonable search range
    left: float = -1000.0
    right: float = 1000.0

    # Ensure we have opposite signs or zero at boundaries
    while evaluate(left) * evaluate(right) > 0 and right - left > 1e-9:
        left *= 2
        right *= 2

    # Binary search for the root
    for _ in range(100):  # Sufficient precision for the required accuracy
        mid = (left + right) / 2.0
        if evaluate(mid) == 0.0:
            return mid
        if evaluate(left) * evaluate(mid) < 0:
            right = mid
        else:
            left = mid

    return (left + right) / 2.0