def monotonic(l: List[int]) -> bool:
    if len(l) <= 1:
        return True
    inc = all(l[i] <= l[i+1] for i in range(len(l)-1))
    dec = all(l[i] >= l[i+1] for i in range(len(l)-1))
    return inc or dec