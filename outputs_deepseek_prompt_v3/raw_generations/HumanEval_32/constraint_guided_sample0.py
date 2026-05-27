import math
from typing import List


def poly(xs: List[float], x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))


def find_zero(xs: List[int]) -> float:
    """
    Find a real zero of the polynomial with coefficients xs.
    
    Args:
        xs: List of polynomial coefficients where xs[i] is the coefficient for x^i.
            Must have even length and largest non-zero coefficient to guarantee a solution.
    
    Returns:
        A real number x such that poly(xs, x) ≈ 0.
    
    Raises:
        ValueError: If xs doesn't meet the constraints.
    """
    if len(xs) % 2 != 0:
        raise ValueError("Coefficient list must have even length")
    
    if xs[-1] == 0:
        raise ValueError("Largest coefficient must be non-zero")
    
    # Use bisection method to find a root
    # Polynomials with even degree and non-zero leading coefficient have opposite signs at ±∞
    left = -1.0
    right = 1.0
    
    # Expand search interval until we find opposite signs
    while poly(xs, left) * poly(xs, right) > 0:
        left *= 2
        right *= 2
    
    # Bisection method
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
    
    return (left + right) / 2