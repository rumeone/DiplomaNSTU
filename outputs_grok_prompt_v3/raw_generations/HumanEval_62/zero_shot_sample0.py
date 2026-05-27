def derivative(xs: List[int]) -> List[int]:
    return [i * xs[i] for i in range(1, len(xs))]