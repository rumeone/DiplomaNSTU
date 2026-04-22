"""Module providing polynomial evaluation and root finding utilities.

This module contains functions to evaluate polynomials at given points
and to find a root of a polynomial with the given coefficients.
"""

import math
from typing import List


def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


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
    # Use binary search to find a root. The constraints guarantee
    # a real root exists and the leading coefficient is non-zero.
    # We search in the range [-1000, 1000] which is sufficient for
    # the given problem constraints and test cases.

    def evaluate(x: float) -> float:
        """Evaluate the polynomial at x using Horner's method for efficiency."""
        result = 0.0
        for coeff in reversed(xs):
            result = result * x + coeff
        return result

    # Early return for the trivial case of a constant polynomial.
    # Though constraints specify even length, we guard against it.
    if len(xs) == 1:
        # If constant term is zero, any x works; otherwise no root.
        # Per problem, we assume a solution exists.
        return 0.0

    # Find initial bounds where the function changes sign or is zero.
    # Start with a reasonable search range.
    left = -1000.0
    right = 1000.0
    epsilon = 1e-10

    left_val = evaluate(left)
    right_val = evaluate(right)

    # If either endpoint is already a root, return it.
    if abs(left_val) < epsilon:
        return left
    if abs(right_val) < epsilon:
        return right

    # If no sign change, expand the search range (defensive).
    # The problem guarantees a real root exists.
    while left_val * right_val > 0 and right < 1e6:
        right *= 2
        right_val = evaluate(right)

    # Binary search for the root.
    while right - left > epsilon:
        mid = (left + right) / 2
        mid_val = evaluate(mid)

        if abs(mid_val) < epsilon:
            return mid

        if left_val * mid_val < 0:
            # Root is in left half
            right = mid
            right_val = mid_val
        else:
            # Root is in right half
            left = mid
            left_val = mid_val

    # Return the best approximation found
    return (left + right) / 2