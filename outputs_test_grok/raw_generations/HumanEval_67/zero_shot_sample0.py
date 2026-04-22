def fruit_distribution(s: str, n: int) -> int:
    words = s.split()
    apples = 0
    oranges = 0
    for i, word in enumerate(words):
        if word == "apples" or word == "apple":
            apples = int(words[i-1])
        elif word == "oranges" or word == "orange":
            oranges = int(words[i-1])
    return n - apples - oranges