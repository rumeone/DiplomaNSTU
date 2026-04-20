def fruit_distribution(s: str, n: int) -> int:
    words = s.split()
    apples = oranges = 0
    for i, word in enumerate(words):
        if word == "apples":
            apples = int(words[i-1])
        elif word == "oranges":
            oranges = int(words[i-1])
    return n - apples - oranges