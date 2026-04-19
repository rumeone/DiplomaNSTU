def triangle_area(a: float, h: float) -> float:
    if a <= 0 or h <= 0:
        raise ValueError("Side length and height must be positive.")
    return 0.5 * a * h