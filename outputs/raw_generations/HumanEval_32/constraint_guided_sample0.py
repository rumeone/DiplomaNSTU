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

    Examples:
        >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
        -0.5
        >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
        1.0
    """
    # Ensure the polynomial has even degree (odd number of coefficients)
    if len(xs) % 2 != 0:
        raise ValueError("List xs must have an even number of coefficients")

    # Ensure the highest coefficient is non-zero
    if xs[-1] == 0:
        raise ValueError("Largest coefficient must be non-zero")

    # Polynomial has odd degree (since len(xs) is even, degree = len(xs)-1 is odd)
    # Odd degree polynomials are guaranteed to have at least one real root
    # Use bisection method to find a root

    # Find initial bounds where polynomial changes sign
    # Start with a symmetric interval around zero
    left = -1.0
    right = 1.0

    # Expand interval until we find a sign change
    while poly(xs, left) * poly(xs, right) > 0:
        left *= 2
        right *= 2

    # Perform bisection
    tolerance = 1e-10
    max_iterations = 1000

    for _ in range(max_iterations):
        mid = (left + right) / 2
        f_mid = poly(xs, mid)

        if abs(f_mid) < tolerance:
            return mid

        f_left = poly(xs, left)

        if f_left * f_mid <= 0:
            right = mid
        else:
            left = mid

    # Return the midpoint if max iterations reached
    return (left + right) / 2