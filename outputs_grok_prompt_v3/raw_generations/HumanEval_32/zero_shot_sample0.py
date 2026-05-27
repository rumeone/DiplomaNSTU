def find_zero(xs: List[int]) -> float:
    def p(x): return poly(xs, x)
    lo, hi = -1.0, 1.0
    while p(lo) * p(hi) > 0:
        lo *= 2
        hi *= 2
    for _ in range(100):
        mid = (lo + hi) / 2
        if p(lo) * p(mid) > 0:
            lo = mid
        else:
            hi = mid
    return lo