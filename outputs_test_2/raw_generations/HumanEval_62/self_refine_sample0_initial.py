"""Module for polynomial derivative calculation."""

from typing import List


def derivative(xs: List[int]) -> List[int]:
    """
    Compute the derivative of a polynomial given its coefficients.

    The polynomial is represented as:
        xs[0] + xs[1] * x + xs[2] * x^2 + xs[3] * x^3 + ...

    The derivative is computed term by term:
        d/dx (xs[n] * x^n) = n * xs[n] * x^(n-1)

    Args:
        xs: List of polynomial coefficients where xs[i] is the coefficient for x^i.

    Returns:
        List of coefficients for the derivative polynomial.

    Examples:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
        >>> derivative([5])
        []
        >>> derivative([])
        []
    """
    if len(xs) <= 1:
        return []

    derivative_coeffs = []
    for power, coeff in enumerate(xs[1:], start=1):
        derivative_coeffs.append(power * coeff)

    return derivative_coeffs