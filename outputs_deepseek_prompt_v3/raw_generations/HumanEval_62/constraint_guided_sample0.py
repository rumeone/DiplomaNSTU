from typing import List


def derivative(xs: List[int]) -> List[int]:
    """
    Compute the derivative of a polynomial represented by its coefficients.

    The polynomial is represented as:
        xs[0] + xs[1] * x + xs[2] * x^2 + xs[3] * x^3 + ...

    The derivative is computed term by term:
        For term i: coefficient = xs[i] * i, exponent = i-1
        The constant term (i=0) disappears in the derivative.

    Args:
        xs: List of polynomial coefficients where index represents exponent.

    Returns:
        List of coefficients of the derivative polynomial.

    Examples:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    if len(xs) <= 1:
        return []

    derivative_coeffs = []
    for exponent, coefficient in enumerate(xs[1:], start=1):
        derivative_coeffs.append(coefficient * exponent)

    return derivative_coeffs