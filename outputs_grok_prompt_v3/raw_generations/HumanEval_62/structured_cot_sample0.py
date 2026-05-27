from typing import List


"""Compute the derivative of a polynomial represented by its coefficients."""


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
    return [i * coeff for i, coeff in enumerate(xs[1:], start=1)]