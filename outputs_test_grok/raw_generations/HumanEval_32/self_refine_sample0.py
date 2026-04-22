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
    # Use binary search to find a root. The constraints guarantee a real root exists.
    # We search in the range [-1000, 1000] which is sufficient for the given constraints.

    def evaluate(x: float) -> float:
        """Evaluate the polynomial at x using Horner's method for better numerical stability."""
        result = 0.0
        for coeff in reversed(xs):
            result = result * x + coeff
        return result

    # Early return for trivial case
    if len(xs) == 0:
        raise ValueError("Coefficient list cannot be empty")

    # If constant term is zero, then x=0 is a root
    if xs[0] == 0:
        return 0.0

    low = -1000.0
    high = 1000.0
    tolerance = 1e-10
    max_iterations = 100

    for _ in range(max_iterations):
        mid = (low + high) / 2.0
        value = evaluate(mid)

        if abs(value) < tolerance:
            return mid

        # Determine which half to search based on sign change
        # Since we have even degree with positive leading coefficient,
        # the polynomial goes to +inf as x -> +/- inf
        if value > 0:
            # If the leading coefficient is negative, we need to flip the logic
            if xs[-1] < 0:
                low = mid
            else:
                high = mid
        else:
            if xs[-1] < 0:
                high = mid
            else:
                low = mid

    # Return the best approximation found
    return (low + high) / 2.0