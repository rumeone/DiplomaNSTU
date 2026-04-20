from typing import List


def derivative(xs: List[int]) -> List[int]:
    """
    xs represents the coefficients of a polynomial:
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return the derivative of this polynomial in the same form.
    """
    if len(xs) <= 1:
        return []
    
    result = []
    for i in range(1, len(xs)):
        result.append(xs[i] * i)
    
    return result