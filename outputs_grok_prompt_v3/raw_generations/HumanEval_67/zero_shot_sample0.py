def fruit_distribution(s: str, n: int) -> int:
    parts = s.split()
    apples = int(parts[0])
    oranges = int(parts[3])
    return n - apples - oranges