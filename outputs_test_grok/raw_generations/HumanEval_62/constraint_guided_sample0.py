"""Module providing a function to compute the derivative of a polynomial given by its coefficients."""

from typing import List


def derivative(xs: List[int]) -> List[int]:
    """
    xs represents the coefficients of a polynomial:
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return the derivative of this polynomial in the same form.

    Examples:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    if len(xs) <= 1:
        return []

    # Compute derivative coefficients: deriv[i] = (i + 1) * xs[i + 1]
    return [(i + 1) * xs[i + 1] for i in range(len(xs) - 1)]