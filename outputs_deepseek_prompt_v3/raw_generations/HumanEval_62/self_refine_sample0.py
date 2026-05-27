"""
Polynomial derivative calculation.

This module provides a function to compute the derivative of a polynomial
represented by its coefficients.
"""

from typing import List


def derivative(xs: List[int]) -> List[int]:
    """
    Compute the derivative of a polynomial given its coefficients.

    The polynomial is represented as:
        xs[0] + xs[1] * x + xs[2] * x^2 + xs[3] * x^3 + ...

    The derivative is returned in the same coefficient representation.

    Args:
        xs: List of integer coefficients where xs[i] is the coefficient for x^i.

    Returns:
        List of integer coefficients for the derivative polynomial.

    Examples:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    if len(xs) <= 1:
        return []

    derivative_coeffs = []
    for power, coeff in enumerate(xs[1:], start=1):
        derivative_coeffs.append(coeff * power)

    return derivative_coeffs