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
    # Since the polynomial has even degree with positive leading coefficient
    # (as per constraints), it goes to +inf as x -> +/- inf.
    # We search in [-1000, 1000] which is sufficient for the given constraints.
    
    def evaluate(x: float) -> float:
        return poly(xs, x)
    
    # Find interval where sign changes or a root
    low = -1000.0
    high = 1000.0
    mid = 0.0
    eps = 1e-10
    
    # First check if zero is a root
    if abs(evaluate(0.0)) < eps:
        return 0.0
    
    # Binary search for root
    for _ in range(100):  # High precision with fixed iterations
        mid = (low + high) / 2.0
        if evaluate(mid) == 0:
            return mid
        elif evaluate(low) * evaluate(mid) < 0:
            high = mid
        else:
            low = mid
    
    return mid