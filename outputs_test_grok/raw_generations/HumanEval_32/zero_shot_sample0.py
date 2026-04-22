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
    # Use binary search to find a root.
    # Since the polynomial has even degree with positive leading coefficient,
    # it goes to +inf as x -> +/- inf. We need to find an interval where it changes sign.
    
    def evaluate(x: float) -> float:
        return poly(xs, x)
    
    # Start with a reasonable search range
    left = -1000.0
    right = 1000.0
    
    # First find an interval where the function changes sign
    while right - left > 1e-9:
        mid = (left + right) / 2
        if evaluate(left) * evaluate(mid) > 0:
            left = mid
        else:
            right = mid
    
    # Now do binary search for the root in the interval [left, right]
    left = -10000.0
    right = 10000.0
    for _ in range(100):  # High precision binary search
        mid = (left + right) / 2
        if evaluate(mid) * evaluate(left) <= 0:
            right = mid
        else:
            left = mid
    
    return (left + right) / 2