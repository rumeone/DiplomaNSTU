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

    left = -1.0
    right = 1.0

    while poly(xs, left) * poly(xs, right) > 0:
        left *= 2
        right *= 2

    for _ in range(100):
        mid = (left + right) / 2
        if poly(xs, mid) == 0:
            return mid
        if poly(xs, left) * poly(xs, mid) < 0:
            right = mid
        else:
            left = mid

    return (left + right) / 2