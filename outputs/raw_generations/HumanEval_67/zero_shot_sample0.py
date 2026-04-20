def fruit_distribution(s: str, n: int) -> int:
    import re
    numbers = list(map(int, re.findall(r'\d+', s)))
    return n - sum(numbers)