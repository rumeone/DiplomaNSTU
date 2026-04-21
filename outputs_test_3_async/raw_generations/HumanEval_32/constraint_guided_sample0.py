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
    if len(xs) % 2 != 0:
        raise ValueError("Coefficient list must have even length")
    if xs[-1] == 0:
        raise ValueError("Largest coefficient must be non-zero")

    def polynomial_value(x_val: float) -> float:
        return sum(coeff * (x_val ** i) for i, coeff in enumerate(xs))

    left_bound = -1.0
    right_bound = 1.0

    while polynomial_value(left_bound) * polynomial_value(right_bound) > 0:
        left_bound *= 2
        right_bound *= 2

    tolerance = 1e-10
    max_iterations = 1000

    for _ in range(max_iterations):
        midpoint = (left_bound + right_bound) / 2
        mid_value = polynomial_value(midpoint)

        if abs(mid_value) < tolerance:
            return midpoint

        left_value = polynomial_value(left_bound)
        if left_value * mid_value <= 0:
            right_bound = midpoint
        else:
            left_bound = midpoint

    return (left_bound + right_bound) / 2