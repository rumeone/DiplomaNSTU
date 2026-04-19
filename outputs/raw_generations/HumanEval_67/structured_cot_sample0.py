def fruit_distribution(s: str, n: int) -> int:
    import re
    numbers = re.findall(r'\d+', s)
    total_apples_oranges = sum(int(num) for num in numbers)
    return n - total_apples_oranges