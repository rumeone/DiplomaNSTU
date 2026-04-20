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
    n = len(xs) - 1
    while xs[n] == 0:
        n -= 1

    def f(x: float) -> float:
        return poly(xs, x)

    def derivative(x: float) -> float:
        return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])

    x0 = 0.0
    for _ in range(100):
        fx = f(x0)
        if abs(fx) < 1e-12:
            return x0
        dfx = derivative(x0)
        if dfx == 0:
            x0 += 0.1
            continue
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < 1e-12:
            return x1
        x0 = x1
    return x0