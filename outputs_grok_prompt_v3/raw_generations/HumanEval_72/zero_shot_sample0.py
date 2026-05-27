def will_it_fly(q: List[int], w: int) -> bool:
    if not q:
        return 0 <= w
    start = 0
    while start < len(q) and q[start] == 0:
        start += 1
    end = len(q) - 1
    while end >= start and q[end] == 0:
        end -= 1
    if start > end:
        effective = []
    else:
        effective = q[start:end + 1]
    is_pal = effective == effective[::-1]
    total_sum = sum(q)
    return is_pal and total_sum <= w