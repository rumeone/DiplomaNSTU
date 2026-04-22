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
    def f(x: float) -> float:
        return poly(xs, x)

    # Use bisection method. Since degree is even and leading coefficient
    # is non-zero, there is at least one real root.
    # Start with a wide interval that is guaranteed to contain a root.
    low = -1000.0
    high = 1000.0
    while high - low > 1e-6:
        mid = (low + high) / 2.0
        if f(mid) * f(low) > 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2.0