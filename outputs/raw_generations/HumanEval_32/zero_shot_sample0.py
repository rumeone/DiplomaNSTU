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
    n = len(xs)
    if n % 2 != 0:
        raise ValueError("List xs must have an even number of coefficients")
    
    # Find the largest non-zero coefficient
    max_coeff_idx = n - 1
    while xs[max_coeff_idx] == 0:
        max_coeff_idx -= 1
    
    # The polynomial degree is max_coeff_idx
    # For even degree polynomials, we can use bisection method
    # We'll search between -100 and 100 as reasonable bounds
    left = -100.0
    right = 100.0
    
    # Ensure poly(left) and poly(right) have opposite signs
    # If not, expand bounds
    f_left = poly(xs, left)
    f_right = poly(xs, right)
    
    # Adjust bounds if signs are same
    while f_left * f_right > 0:
        left *= 2
        right *= 2
        f_left = poly(xs, left)
        f_right = poly(xs, right)
    
    # Bisection method
    for _ in range(100):  # 100 iterations for precision
        mid = (left + right) / 2
        f_mid = poly(xs, mid)
        if abs(f_mid) < 1e-12:
            return mid
        if f_left * f_mid <= 0:
            right = mid
            f_right = f_mid
        else:
            left = mid
            f_left = f_mid
    
    return (left + right) / 2